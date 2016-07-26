
class Station(object):
    
    
    def __init__(self, universe, data):
        
        self.universe                   = universe
        self.uid                        = data[0]
        self.security                   = data[1]
        self.dockingCostPerVolume       = data[2]
        self.maxShipVolumeDockable      = data[3]
        self.officeRentalCost           = data[4]
        self.operationID                = data[5]
        self.stationTypeID              = data[6]
        self.corporationID              = data[7]
        self.solarSystemID              = data[8]
        self.constellationID            = data[9]
        self.regionID                   = data[10]
        self.name                       = data[11]
        self.x                          = data[12]
        self.y                          = data[13]
        self.z                          = data[14]
        self.reprocessingEfficiency     = data[15]
        self.reprocessingStationsTake   = data[16]
        self.reprocessingHangarFlag     = data[17]


    @property
    def system(self):
        return self.universe.system[self.solarSystemID]
    

    @property
    def constellation(self):
        return self.universe.constellation[self.constellationID]
    

    @property
    def region(self):
        return self.universe.region[self.regionID]
    

    @property
    def stationType(self):
        return self.universe.stationType[self.stationTypeID]
