import shelve
import connect_database

user_info = shelve.open("user_information.shelve", writeback=True)
#connect_database.delete_group(0, user_info)

user_info.close()