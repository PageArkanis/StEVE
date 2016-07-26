from steve.backend.sqlitedb import SDB
from steve.race import Race
from steve.attribute import Attribute


class Attributes(object):


    def __init__(self):

        self._races              = {}
        self._attributes         = {}



    @property
    def race(self):
        
        if len(self._races) == 0:
            query = 'SELECT * from chrRaces'
            for entry in SDB.queryAll(query):
                obj = Race(self, entry)
                self._races[obj.name] = obj
                self._races[obj.uid]  = obj

        return self._races


    @property
    def attribute(self):
        
        if len(self._attributes) == 0:
            query = 'SELECT * from chrAttributes'
            for entry in SDB.queryAll(query):
                obj = Attribute(self, entry)
                self._attributes[obj.name] = obj
                self._attributes[obj.uid]  = obj

        return self._attributes


