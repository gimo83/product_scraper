from app import Base

class Product(Base):
    _table = 'product'
    name = None
    desc = None
    barcode = None
    
    
    def test(self):
        pass
