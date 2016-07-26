from steve.backend.sqlitedb import SDB
from steve.item             import Item
from steve.type             import Type
from steve.market_group     import MarketGroup


class Assets(object):

    
    def __init__(self):
        self._types              = {}   #  { <uid>/<name> : Type  }
        self._items              = {}   #  { <uid>/<name> : Item  } 
        self._blueprints         = {}   #  { <uid>/<name> : Type  }
        self._marketGroups       = {}   #  { <uid> : MarketGroup  }
        self._marketGroupsByName = {}   #  { <name> : [MarketGroup*]  }
        self._flags              = {}   #  { <uid> : <name> }
        self._unique_names       = {}   #  { <uid> : <name>, <name> : <uid> }

        self.testMarketGroup = MarketGroup(self, [-1, None, 'Test', '', 0, True])
        
        
    @property
    def type(self):
        
        if len(self._types) == 0:
            for entry in SDB.queryAll('SELECT * from invTypes'):
                _type = Type(self, entry)
                self._types[_type.uid]  = _type
                self._types[_type.name] = _type
        
        return self._types


    @property
    def types(self):
        return [v for k, v in self.type.items() if isinstance(k, int)]

    
    @property
    def item(self):
        
        if len(self._items) == 0:
            for entry in SDB.queryAll('SELECT * from invItems'):
                item = Item(self, entry)
                self._items[item.uid]  = item
        
        return self._items
    
    
    @property
    def blueprint(self):
        
        if len(self._blueprints) == 0:
            query = 'SELECT typeID from industryActivity WHERE activityID = 5'
            for entry in SDB.queryAll(query):
                _object = self.type.get(entry[0])
                if _object:
                    self._blueprints[_object.name] = _object
                    self._blueprints[_object.uid]  = _object
        
        return self._blueprints


    @property
    def marketGroups(self):
        
        if len(self._marketGroups) == 0:
            for entry in SDB.queryAll('SELECT * FROM invMarketGroups'):
                obj = MarketGroup(self, entry)
                self._marketGroups[obj.uid]  = obj
                
                if obj.name not in self._marketGroupsByName:
                    self._marketGroupsByName[obj.name] = []
                self._marketGroupsByName[obj.name].append(obj)

        return self._marketGroups


    @property
    def marketGroupsByName(self):
        if len(self._marketGroupsByName) == 0:
            _ = self.marketGroups
        return self._marketGroupsByName


    @property
    def inventoryFlag(self):
        if len(self._flags) == 0:
            for entry in SDB.queryAll('SELECT flagID, flagText FROM invFlags'):
                self._flags[entry[0]] = entry[1]
        return self._flags


    @property
    def uname(self):
        if len(self._unique_names) == 0:
            for entry in SDB.queryAll('SELECT * FROM invUniqueNames'):
                self._unique_names[entry[0]]  = entry[1]
                self._unique_names[entry[1]]  = entry[2]
 
        return self._unique_names
        
