from tinydb import TinyDB

db = TinyDB('./db.json')

from app.models import Base

from app.models.product import Product

