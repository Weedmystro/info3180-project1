
# Global Imports
from . import db

# Class for Database


class Property(db.Model):

    # Attributes
    __tablename__ = 'Properties'  # Table Name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text())
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    p_type = db.Column(db.String(20))
    location = db.Column(db.String(200), unique=True)
    photo = db.Column(db.String(150))

    # Constructor
    def __init__(self, title, description, bedrooms, bathrooms, price, p_type, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.p_type = p_type
        self.location = location
        self.photo = photo
    # --------------------------------------------------------------------

    # Other Methods
    def __repr__(self):
        return '<Property %r>' % self.title

    def get_id(self):
        return str(self.id)
