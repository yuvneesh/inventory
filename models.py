from inventory import db

class MaterialsList(db.Model):
    Product = db.Column(db.String, primary_key = True)
    CatalogNumber = db.Column(db.String, nullable=False)