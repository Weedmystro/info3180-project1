
# Global Imports
from . import db

# Class for Database

class Property(db.Model):

    # Attributes
    __tablename__ = 'Properties'  # Table Name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text(1400))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    pType = db.Column(db.String(75))
    location = db.Column(db.String(255), unique=True)
    image = db.Column(db.String(75))

    # Constructor
    def __init__(self, title, description, bedrooms, bathrooms, price, pType, location, image):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.pType = pType
        self.location = location
        self.image = image
    # --------------------------------------------------------------------

    # Other Methods
    def __repr__(self):
        return '<Property %r>' % self.title

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
