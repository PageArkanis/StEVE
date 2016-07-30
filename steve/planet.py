

class Planet(object):
    
    
    
    def __init__(self, universe, data):
        self.universe        = universe
        self.uid             = data[0]
        self.typeID          = data[1]
        self.systemID        = data[3]
        self.constellationID = data[4]
        self.regionID        = data[5]
        self.orbitID         = data[6]
        self.x               = data[7]
        self.y               = data[8]
        self.z               = data[9]
        self.radius          = data[10]
        self.name            = data[11]
        self.security        = data[12]
        self.celestialIndex  = data[13]
        

    @property
    def system(self):
        return self.universe.system[self.systemID]

    @property
    def constellation(self):
        return self.universe.constellation[self.constellationID]

    @property
    def region(self):
        return self.universe.region[self.regionID]
