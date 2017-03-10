#import simplejson as json
from tinydb.database import Element
from app import db

class Base(Element):
    def __init__(self):
        pass

    @classmethod
    def get(self,eid):
        _result = None
        _db = self._getTable()
        if eid != None:
            _result = _db.get(eid=eid)
            
        return _result

    @classmethod
    def all(self):
        return self._getTable().all()

    def save(self):
        _db = self._getTable()
        if hasattr(self,'eid') and self.eid != None :
            _db.update(self.__dict__)
        else:
            _db.insert(self)

    @classmethod        
    def _getTableName(self):
        _tableName = self.__class__.__name__
        if hasattr(self, '_table') and self._table != None:
            _tableName = self._table
        
        return _tableName

    @classmethod
    def _getTable(self):
        return db.table(self._getTableName())
