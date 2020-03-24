'''Stores database models (classes to contain information retrieved from the
database.'''
from flask_login import UserMixin
from dnd_app import login, mysql


class User(UserMixin):
    '''Database model to hold user information from the database'''
    id = 0
    account_name = ''
    password = ''
    email = ''

    def load_with_id(self, account_id):
        '''Loads User object from account id'''
        ## Run mysql query for account relation.
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM account WHERE id=%s", (account_id,))
        uservalues = cursor.fetchone()
        cursor.close()
        ## Populate Object.
        self.id = uservalues['id']
        self.account_name = uservalues['accountName']
        self.password = uservalues['password']
        self.email = uservalues['email']

    def load_with_login(self, account_name):
        '''Loads User object from username'''
        ## Run mysql query for account relation.
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM account WHERE accountName=%s", (account_name,))
        uservalues = cursor.fetchone()
        cursor.close()
        ## Populate Object.
        self.id = uservalues['id']
        self.account_name = uservalues['accountName']
        self.password = uservalues['password']
        self.email = uservalues['email']


@login.user_loader
def load_user(id):
    return User().load_with_id(int(id))
