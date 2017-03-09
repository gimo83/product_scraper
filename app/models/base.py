#import simplejson as json
import json
from app import db

class Base():
    def __init__(self):
        #self._db = db.table(self._table)
        pass
    
    def find(self):
        pass

    def save(self):
        _db = db.table(self._table)
        #print(json.dumps(self))
        if '_id' in self.__dict__:
            _db.update(self.__dict__)
        else:
            _db.insert(self.__dict__)
