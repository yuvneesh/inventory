from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class MaterialsList(db.Model):
    Product = db.Column(db.String, primary_key = True)
    CatalogNumber = db.Column(db.String, nullable=False)