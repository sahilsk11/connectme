#!/usr/bin/python

print "Content-type: application/json\n\n"

import shelve
import json
import cgi
import group
import user

def init_shelve(f):
    if (not "groups" in f):
        f["groups"] = []
    if (not "users" in f):
        f["users"] = {}
    
def create_group(event_name, date, categories, description, location, host, maximum_people, fb_url,  f):
    s = group.Group(event_name, date, categories, description, location, host, 2, fb_url)
    f["groups"].insert(0, s)
    
def delete_group(index, f):
    print(len(f["groups"]))
    f["groups"].remove(1)
    
def add_user(user_name, first_name, last_name, password, email_address, phone, linkedin, facebook, github, f):
    #if (not user_name in f["users"]):
    #    new_user = user.User(user_name, first_name, last_name, email_address, phone)
    #    f["users"][user_name] = new_user
    #    return new_user
    #else:
    #    return None
    new_user = user.User(user_name, first_name, last_name, password, email_address, phone, linkedin, facebook, github)
    f["users"][user_name] = new_user
    return new_user

def delete_event(index, f):
    del f["groups"][index]

def add_user_to_event(username, code, f):
    applicant = f["users"][username]
    for event in f["groups"]:
        if (str(event.uid) == code):
            found = False
            for users in event.applied_users:
                if (users.username == username):
                    found = True
            if (not found):
                event.applied_users.append(applicant)
    
def create_dict_from_group(group):
    d = {}
    d["name"] = group.name
    d["uid"] = group.uid
    d["group_date"] = group.group_date
    d["categories"] = group.categories
    d["description"] = group.description
    d["location"] = group.location
    d["host"] = {}
    d["host"]["name"] = group.host.first_name + " " + group.host.last_name
    d["host"]["host_id"] = group.host.username
    d["maximum_people"] = group.maximum_people
    d["fb_url"] = group.fb_url
    d["applied_users"] = list(group.applied_users)
    for i in range(0, len(d["applied_users"])):
        d["applied_users"][i] = d["applied_users"][i].__dict__
        
    d["accepted_users"] = list(group.applied_users)
    for i in range(0, len(d["accepted_users"])):
        d["accepted_users"][i] = d["accepted_users"][i].__dict__
    return d
        
user_data = shelve.open("user_information.shelve", writeback=True)
init_shelve(user_data)
form = cgi.FieldStorage()
command = form.getfirst("command", "")
code = form.getfirst("code", "")
data = form.getfirst("data", "")
username = form.getfirst("username", "")
password = form.getfirst("password", "")
host = form.getfirst("host", "")

if (command == "events"):
    sorted_groups = []
    for i in range(0, len(user_data["groups"])):
        group_dict = create_dict_from_group(user_data["groups"][i])
        sorted_groups.append(group_dict)
    j = json.dumps(sorted_groups)
    print j
    
if (command == "create"):
    d = eval(data)
    user_host = d["host"]
    event_host = user_data["users"][user_host]
    create_group(d["event_name"], d["event_date"], "", d["description"], d["location"], event_host, d["maximum_people"], d["fb_url"], user_data)
    d = {"success":"true"}
    j = json.dumps(d)
    print j
    
if (command == "single_event"):
    j = ""
    for i in range (0, len(user_data["groups"])):
        if (str(user_data["groups"][i].uid) == code):
            d = create_dict_from_group(user_data["groups"][i])
            j = json.dumps(d)
    print j
    
if (command == "user_information"):
    user = user_data["users"][code]
    if (user != None):
        d = user.__dict__
        j = json.dumps(d)
        print j
    else:
        print {"error":"not_found"}
        
if (command == "create-user"):
    d = eval(data)
    add_user(d["username"], d["first_name"], d["last_name"], d["password"], d["email"], d["phone_number"], d["linkedin"], d["facebook"], d["github"], user_data)
    d = {"success":"true"}
    j = json.dumps(d)
    print j
    
if (command == "apply-user"):
    add_user_to_event(username, code, user_data)
    d = {"success":"true"}
    j = json.dumps(d)
    print j
    
if (command == "delete_event"):
    event = None
    for i in range (0, len(user_data["groups"])):
        if (str(user_data["groups"][i].uid) == code):
            delete_event(i, user_data)

if (command == "login"):
    d = {}
    if not (username in user_data["users"]):
        d["success"] = False
    else:
        p = user_data["users"][username].password
        if (p == password):
            d["success"] = True
            d["username"] = username
        else:
            d["success"] = False
    j = json.dumps(d)
    print j

user_data.close()