import shelve
import group

user_info = shelve.open("user_information.shelve", writeback=True)
print(user_info["groups"][0])

user_info.close()