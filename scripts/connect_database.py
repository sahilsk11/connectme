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
    
def create_group(f, host):
    s = group.Group("Basketball Party", "6/20", ["sports"], "description", "San Jose", host, 2, "")
    f["groups"].insert(0, s)
    
def add_user(user_name, first_name, last_name, email_address, f):
    if (not user_name in f["users"]):
        new_user = user.User(user_name, first_name, last_name, email_address)
        f["users"][user_name] = new_user
        return new_user
    else:
        return None
    
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
    d["host"]["host_id"] = group.host.user_name
    d["maximum_people"] = group.maximum_people
    d["fb_url"] = group.fb_url
    d["applied_users"] = group.applied_users
    d["accepted_users"] = group.applied_users
    return d
        
user_data = shelve.open("user_information.shelve", writeback=True)
#user_data.clear()
init_shelve(user_data)
#host = add_user("sahil", "Sahil", "Kapur", "", user_data)
#create_group(user_data, host)
form = cgi.FieldStorage()
command = form.getfirst("command", "")
code = form.getfirst("code", "")

if (command == "events"):
    sorted_groups = []
    for i in range(0, len(user_data["groups"])):
        group_dict = create_dict_from_group(user_data["groups"][i])
        sorted_groups.append(group_dict)
    j = json.dumps(sorted_groups)
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

user_data.close()