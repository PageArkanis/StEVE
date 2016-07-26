

class System(object):
    
    
    def __init__(self, universe, data):
        
        self.universe        = universe
        self.regionID        = data[0]
        self.constellationID = data[1]
        self.uid             = data[2]
        self.name            = data[3]
        self.x               = data[4]
        self.y               = data[5]
        self.z               = data[6]
        self.xMin            = data[7]
        self.xMax            = data[8]
        self.yMin            = data[9]
        self.yMax            = data[10]
        self.zMin            = data[11]
        self.zMax            = data[12]
        self.factionID       = data[13]
        self.radius          = data[14]


    @property
    def constellation(self):
        return self.universe.constellation[self.constellationID]
    
    
    @property
    def region(self):
        return self.universe.region[self.regionID]
