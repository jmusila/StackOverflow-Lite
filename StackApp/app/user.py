class User(object):

    def __init__(self):
        self.users = []

    def create_user(self, user_id, names, username, email, password):
        new_user = {
            'user_id': user_id,
            'names':names,
            'username': username,
            'email': email,
            'password': password,
            'login_status':False
        }

        self.users.append(new_user)

        return self.users