from . import db
from flask_login import UserMixin   

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150))
    caption=db.Column(db.String(1500))
    #imagename=db.Column(db.String(),nullable=False)
    #image=db.Column(db.LargeBinary)
    #time=db.Column(db.Time(timezone=True),default=func.now())

    def __init__(self,title,caption):
        self.title=title
        self.caption=caption
        #self.imagename=imagename

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
