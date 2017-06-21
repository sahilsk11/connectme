import datetime
import shelve
import random

class Group:
        
    def __init__(self, name, date, categories, description, location, host, maximum_people=None, fb_url=None):
        self.name = name
        self.uid = self.create_uid()
        self.group_date = date
        self.categories = categories
        self.description = description
        self.location = location
        self.host = host
        self.maximum_people = maximum_people
        self.fb_url = fb_url
        self.applied_users = []
        self.accepted_users = []
        
    def create_uid(self):
        f = shelve.open("user_information.shelve", writeback=True)
        uids = f["groups"]
        uid = 0
        for i in range(0, 4):
            number = random.randint(1, 9)
            uid = uid * 10 + number
        if (uid not in uids):
            f.close()
            return uid
        else:
            return None
    
    def add_user(self, user):
        if (not self.maximum_people == None and len(self.accepted_users) >= self.maximum_people):
            return False
        self.applied_users.add(user)
        return True
    
    def remove_applied_user(self, index):
        self.applied_users.remove(index)
        
    def remove_accepted_user(self, index):
        self.accepted_users.remove(index)