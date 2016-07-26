from steve.backend.sqlitedb import SDB
from steve.system           import System


class Constellation(object):
    
    
    def __init__(self, universe, data):
        self.universe   = universe

        self.regionID   = data[0]
        self.uid        = data[1]
        self.name       = data[2]
        self.x          = data[3]
        self.y          = data[4]
        self.z          = data[5]
        self.xMin       = data[6]
        self.xMax       = data[7]
        self.yMin       = data[8]
        self.yMax       = data[9]
        self.zMin       = data[10]
        self.zMax       = data[11]
        self.factionID  = data[12]
        self.radius     = data[13]

        self._systems = {}


    @property
    def system(self):
        
        if len(self._constellations) == 0:
            query = 'SELECT * from mapSolarSystems WHERE constellationID = %' % self.uid
            for entry in SDB.queryAll(query):
                system = System(self.universe, entry)
                self._systems[system.name] = system
                self._systems[system.uid]  = system
        
        return self._systems


    @property
    def region(self):
        return self.universe.regions[self.regionID]
