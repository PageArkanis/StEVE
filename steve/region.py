from steve.backend.sqlitedb import SDB

from steve.constellation    import Constellation
from steve.system import System


class Region(object):
    
    
    def __init__(self, universe, data):
        self.universe   = universe
        self.uid        = data[0]
        self.name       = data[1]
        self.x          = data[2]
        self.y          = data[3]
        self.z          = data[4]
        self.xMin       = data[5]
        self.xMax       = data[6]
        self.yMin       = data[7]
        self.yMax       = data[8]
        self.zMin       = data[9]
        self.zMax       = data[10]
        self.factionID  = data[11]
        self.radius     = data[12]

        self._constellations = {}
        self._systems        = {}


    @property
    def constellation(self):
        
        if len(self._constellations) == 0:
            query = 'SELECT * from mapConstellations WHERE regionID = %s' % self.uid
            for entry in SDB.queryAll(query):
                constellation = Constellation(self.universe, entry)
                self._constellations[constellation.name] = constellation
                self._constellations[constellation.uid]  = constellation
            
            
        
        return self._constellations
    

    @property
    def system(self):
        
        if len(self._constellations) == 0:
            query = 'SELECT * from mapSolarSystems WHERE constellationID = %' % self.uid
            for entry in SDB.queryAll(query):
                system = System(self.universe, entry)
                self._systems[system.name] = system
                self._systems[system.uid]  = system
        
        return self._systems
