class User:
    def __init__(self, user_name, first_name, last_name, password, email_address, phone, linkedin, facebook, github):
        self.username = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email_address = email_address
        self.phone = phone
        self.linkedin = linkedin
        self.facebook = facebook
        self.github = github
        
    def change_user_name(self, new_user):
        self.user_name = new_user