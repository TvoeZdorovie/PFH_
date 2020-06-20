from app import db , login_manager
from flask_login import  UserMixin
from hashlib import md5


ROLE_USER = 0
ROLE_ADMIN = 1
SALT = "crazy_secret_salt"

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

class User(db.Model , UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), index = True, unique = True)
    passwd = db.Column(db.String(120) , index = True , unique = False)
    name = db.Column(db.String(120) , index = True , unique = False)
    role = db.Column(db.SmallInteger, default = ROLE_USER)



    def check_password(self , password):
        hash_object = md5((password + SALT).encode())
        if str(hash_object.hexdigest()) == self.passwd:
            return True
        return False

    def hash_password(self):
        hash_object = md5((self.passwd + SALT).encode())
        self.passwd = str(hash_object.hexdigest())
        
    

    