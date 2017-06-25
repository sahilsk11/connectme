import shelve

user_info = shelve.open("user_information.shelve")
print(user_info)
user_info.close()