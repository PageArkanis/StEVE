from steve.backend.sqlitedb import SDB
from steve.region           import Region
from steve.constellation    import Constellation
from steve.system           import System
from steve.station import Station
from steve.station_type import StationType
from steve.planet import Planet


class Universe(object):
    
    
    def __init__(self):
        self._regions            = {}
        self._regionNames        = []

        self._constellations     = {}
        self._constellationNames = []
        
        self._systems            = {}
        self._systemNames        = []
        
        self._stations           = {}
        self._stationNames       = []
        
        self._stationTypes       = {}
        
        self._planets            = {}
        self._planetNames        = []
        

        
    @property
    def region(self):
        
        if len(self._regions) == 0:
            for entry in SDB.queryAll('SELECT * from mapRegions'):
                region = Region(self, entry)
                self._regions[region.name] = region
                self._regions[region.uid]  = region
                self._regionNames.append(region.name)
        
        return self._regions
    

    @property
    def constellation(self):
        
        if len(self._constellations) == 0:
            query = 'SELECT * from mapConstellations'
            for entry in SDB.queryAll(query):
                constellation = Constellation(self, entry)
                self._constellations[constellation.name] = constellation
                self._constellations[constellation.uid]  = constellation
                self._constellationNames.append(constellation.name)
        
        return self._constellations
    

    @property
    def system(self):
        
        if len(self._systems) == 0:
            query = 'SELECT * from mapSolarSystems'
            for entry in SDB.queryAll(query):
                system = System(self, entry)
                self._systems[system.name] = system
                self._systems[system.uid]  = system
                self._systemNames.append(system.name)

        return self._systems


    @property
    def planet(self):
        
        if len(self._planets) == 0:
            query = 'SELECT * from mapDenormalize WHERE groupID = 7'
            for entry in SDB.queryAll(query):
                _obj = Planet(self, entry)
                self._planets[_obj.name] = _obj
                self._planets[_obj.uid]  = _obj
                self._planetNames.append(_obj.name)

        return self._planets

    
    @property
    def regionNames(self):
        if len(self._regionNames) == 0:
            _ = self.regions
        return self._regionNames
    
    
    @property
    def constellationNames(self):
        if len(self._constellationNames) == 0:
            _ = self.constellations
        return self._constellationNames
    

    @property
    def systemNames(self):
        if len(self._systemNames) == 0:
            _ = self.systems
        return self._systemNames
    

    @property
    def planetNames(self):
        if len(self._planetNames) == 0:
            _ = self.planets
        return self._planetNames

    
    @property
    def station(self):
        
        if len(self._stations) == 0:
            query = 'SELECT * from staStations'
            for entry in SDB.queryAll(query):
                obj = Station(self, entry)
                self._stations[obj.name] = obj
                self._stations[obj.uid]  = obj
                self._stationNames.append(obj.name)

        return self._stations


    @property
    def stationType(self):
        
        if len(self._stationTypes) == 0:
            query = 'SELECT * from staStationTypes'
            for entry in SDB.queryAll(query):
                obj = StationType(self, entry)
                self._stationTypes[obj.uid]  = obj

        return self._stationTypes
