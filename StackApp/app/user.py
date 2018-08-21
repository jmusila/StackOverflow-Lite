class User(object):

    def __init__(self):
        self.users = []

    def create_user(self, user_id, name,username, email, password,confirm_password):
        new_user = {
            'user_id': user_id,
            'name': name,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }

        self.users.append(new_user)

        return self.users