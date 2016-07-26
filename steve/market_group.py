from steve.backend.sqlitedb import SDB

class MarketGroup(object):
    
    SQL = ['SELECT typeID FROM invTypes WHERE marketGroupID == %s ORDER BY typeName']
    
    def __init__(self, assets, data):
        
        self.assets             = assets
        self.uid                = data[0]
        self.parentGroupID      = data[1]
        self.name               = data[2]
        self.description        = data[3]
        self.iconID             = data[4]
        self.hasTypes           = data[5]
        self._items             = []


    @property
    def parentMarketGroup(self):
        if self.parentGroupID:
            return self.assets.marketGroup[self.parentGroupID]

    
    @property
    def items(self):
        if len(self._items) == 0:
            from steve import Assets
            for entry in SDB.queryAll(MarketGroup.SQL[0] % self.uid):
                self._items.append(Assets.type[entry[0]])
            
        return self._items