'''Stores database models (classes to contain information retrieved from the
database.'''
from flask_login import UserMixin
from dnd_app import login, mysql


class User(UserMixin):
    '''Database model to hold user information from the database'''
    def __init__(self, key):
        '''Loads User object from account id'''
        ## Run mysql query for account relation.
        cursor = mysql.connection.cursor()
        ## search for id if key is int, search for accountName if string.
        if isinstance(key, int) is True:
            cursor.execute("SELECT * FROM account WHERE id=%s", (key,))
        else:
            cursor.execute("SELECT * FROM account WHERE accountName=%s", (key,))
        uservalues = cursor.fetchone()
        cursor.close()
        ## Populate Object.
        self.id = uservalues['id']
        self.account_name = uservalues['accountName']
        self.password = uservalues['password']
        self.email = uservalues['email']


@login.user_loader
def load_user(id):
    return User(int(id))
