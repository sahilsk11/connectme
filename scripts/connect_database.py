#!usr/bin/python

print "Content-type: application/json\n\n"

import shelve
import json
import cgi
import group

def init_shelve(f):
    if (not "groups" in f):
        f["groups"] = []
    
def create_group(f):
    s = group.Group(None, None, None, None, None, None, None)
    f["groups"].insert(0, s)

user_data = shelve.open("user_information.shelve", writeback=True)
init_shelve(user_data)
form = cgi.FieldStorage()
command = form.getfirst("command", "")

command = "events"

if (command == "events"):
    sorted_groups = []
    for i in range(0, len(user_data["groups"])):
        group_dict = user_data["groups"][i].__dict__
        sorted_groups.append(group_dict)
    j = json.dumps(sorted_groups)
    print j
user_data.close()