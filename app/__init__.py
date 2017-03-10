from tinydb import TinyDB

db = TinyDB('./db.json')

#from . models.base import Base
from . models import Product, Link
