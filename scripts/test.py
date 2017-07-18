import shelve

user_info = shelve.open("user_information.shelve", writeback=True)

print(user_info["users"])

user_info.close()