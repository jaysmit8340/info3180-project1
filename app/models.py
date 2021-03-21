from . import db


class UserProperty(db.Model):
    
    __tablename__ = 'user_proper'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(80))
    desc = db.Column(db.String(255))
    numOfBed= db.Column(db.String(80))
    numOfBath = db.Column(db.String(30))
    pric = db.Column(db.String(80))
    proptype = db.Column(db.String(29))
    location = db.Column(db.String(225))
    photo_name=db.Column(db.String(225), index=True)
    
    
    
    def __init__(self, title, desc, numOfBed, numOfBath, pric, proptype, location, photo_name):
        self.title = title
        self.desc = desc
        self.numOfBed = numOfBed
        self.numOfBath = numOfBath
        self.pric = pric
        self.proptype = proptype
        self.location = location
        self.photo_name=photo_name



    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)