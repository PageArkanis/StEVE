from math                   import ceil

from steve.backend.sqlitedb import SDB
from steve.type             import Type


class Blueprint(Type):
    

    SQL = [
          'SELECT maxProductionLimit FROM industryBlueprints WHERE typeID = %s',
          'SELECT materialTypeID, quantity FROM industryActivityMaterials WHERE typeID = %s AND activityID = 1',
           ]


    def __init__(self, assets, data, copy = False):
        Type.__init__(self, assets, data)
        
        assert self.isBPO, 'data argument has to contain blueprint type data.'
        self._me    = 0
        self._te    = 0
        self._runs  = 0
        self._copy  = copy

        self._maxProductionLimit = None
        

    @property
    def type(self):
        return self._bpo
    

    @property
    def me(self):
        return self._me
    

    @me.setter
    def me(self, value):
        assert int(value) and (0 <= value <= 10), 'ME value out of range [0-10]'
        self._me = value


    @property
    def te(self):
        return self._te
    

    @te.setter
    def te(self, value):
        assert int(value) and (0 <= value <= 10), 'TE value out of range [0-10]'
        self._te = value

    
    @property
    def runs(self):
        self._runs
    

    @property
    def isCopy(self):
        return self._copy
    

    @property
    def maxProductionLimit(self):
        
        if self._maxProductionLimit is None:
            result = SDB.queryOne(Type.SQL[0] % self.uid)
            if result:
                self._maxProductionLimit = result[0]
            else:
                self._maxProductionLimit = 0
                
        return self._maxProductionLimit


    @property
    def requiredMaterials(self):

        result = []
        for entry in SDB.queryAll(Blueprint.SQL[1] % self.uid):
            result.append( ( self.assets.type[entry[0]], 
                             entry[1] * (100.0 - self._me) / 100) )
        return result


    @property
    def meTime(self):
        pass
    
    
    @property
    def teTime(self):
        pass
    
    
    @property
    def buildTime(self):
        pass


    @property
    def copyTime(self):
        pass
