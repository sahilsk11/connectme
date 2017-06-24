#!/usr/bin/python

print "Content-type: application/json\n\n"

import shelve
import json
import cgi
import group

def init_shelve(f):
    if (not "groups" in f):
        f["groups"] = []
    
def create_group(f):
    s = group.Group("Basketball Party", "6/20", ["sports"], "description", "San Jose", "Sahil", 2, "")
    f["groups"].insert(0, s)

user_data = shelve.open("user_information.shelve", writeback=True)
init_shelve(user_data)
form = cgi.FieldStorage()
command = form.getfirst("command", "")
code = form.getfirst("code", "")

if (command == "events"):
    sorted_groups = []
    for i in range(0, len(user_data["groups"])):
        group_dict = user_data["groups"][i].__dict__
        sorted_groups.append(group_dict)
    j = json.dumps(sorted_groups)
    print j
    
if (command == "single_event"):
    j = ""
    for i in range (0, len(user_data["groups"])):
        if (str(user_data["groups"][i].uid) == code):
            d = user_data["groups"][i].__dict__
            j = json.dumps(d)
    print j

user_data.close()