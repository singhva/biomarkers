'''
Created on Jun 13, 2014

@author: varun
'''

from abc import ABCMeta
from abc import abstractmethod
from types import ListType
from types import TupleType
from types import StringType

from bson.objectid import ObjectId

from config import get_db_connection


class DBObject(object):
    
    __metaclass__ = ABCMeta
    COLLECTION = ""
    FK = ""  # Foreign Key (such as Pubmed ID, clinical  trial ID etc.)
    
    def __init__(self, record = None):
        if record:
            self._id = record.get("_id")
            self._record = record
            self._fk = self._get_fk()           
            
        else:
            self._id = None
            self._record = None
            self._fk = None
        
    def get_fk(self):
        return self._fk
    
    def _get_fk(self):
        if self._record:
            if type(self.FK) is StringType:
                fk_path = self.FK.split(".")
                for i, path in enumerate(fk_path):
                    if i == 0:
                        temp = self._record.get(path)
                    else:
                        temp = temp.get(path)       
                return temp
            
            elif type(self.FK) is TupleType:
                return tuple([self._record.get(fk) for fk in self.FK])
    
    def get_db_id(self):
        return self._id
        
    @classmethod
    def db_to_class(cls, record):
        """ This must be implemented """
        raise NotImplementedError()
        
    @abstractmethod
    def class_to_db(self):
        """ This must be implemented """
    
    @classmethod
    def get_by_id(cls, mongo_id):
        db = get_db_connection()
        if isinstance(mongo_id, ObjectId):
            record = db[cls.COLLECTION].find_one({"_id": mongo_id})
        elif isinstance(mongo_id, basestring):
            record = db[cls.COLLECTION].find_one({"_id": ObjectId(mongo_id)})
        return cls.db_to_class(record) if record else None
    
    @classmethod
    def get_all_by_ids(cls, id_list):
        db = get_db_connection()
        mongo_id_list = [ObjectId(_id) for _id in id_list]
        object_list = []
        records = db[cls.COLLECTION].find({"_id":{"$in": mongo_id_list}})
        for record in records:
            obj = cls.db_to_class(record)
            object_list.append(obj)
            
        return object_list
    
    @classmethod
    def get_all_by_fks(cls, fk_list):
        db = get_db_connection()
        object_list = []
        records = db[cls.COLLECTION].find({cls.FK: {"$in": fk_list}})
        for record in records:
            obj = cls.db_to_class(record)
            object_list.append(obj)
            
        return object_list
    
    @classmethod
    def get_by_fk(cls, fk):
        db = get_db_connection()
        if type(cls.FK) is TupleType:
            #print dict(zip(cls.FK, fk))
            record = db[cls.COLLECTION].find_one(dict(zip(cls.FK, fk)))
            print record
        elif type(cls.FK) is StringType:
            record = db[cls.COLLECTION].find_one({cls.FK : fk})
        return cls.db_to_class(record) if record else None
    
    @classmethod
    def get_by_field(cls, fieldname, fieldvalue):
        db = get_db_connection()
        object_list = []
        if isinstance(fieldvalue, basestring):
            record = db[cls.COLLECTION].find_one({fieldname : fieldvalue})
            return cls.db_to_class(record) if record else None
        elif type(fieldvalue) is ListType:
            records = db[cls.COLLECTION].find({fieldname : {"$in" : fieldvalue}})
            for record in records:
                obj = cls.db_to_class(record)
                object_list.append(obj)
            return object_list if len(object_list) > 0 else None
        
        return None
    
    @classmethod
    def dbfind(cls, search_dict):
        db = get_db_connection()
        object_list = []
        records = db[cls.COLLECTION].find(search_dict)
        for record in records:
            obj = cls.db_to_class(record)
            object_list.append(obj)
            
        return object_list
    
    def save(self):
        db = get_db_connection()
        bson = self.class_to_db()
        return db[self.COLLECTION].save(bson, manipulate = True)
    
    # Joins this collections with another collection on other_attr using this collection's foreign key
    def join_with_another_collection(self, other_collection, other_attr):
        db = get_db_connection()
        other_record = db[other_collection].find_one({other_attr : self.get_fk()})
        return other_record

if __name__ == '__main__':
    pass