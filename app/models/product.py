from . base import Base
from . link import Link

class Product(Base):
    _table = 'product'
        
    def getLinks(self):
        return Link.get()
