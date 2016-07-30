from steve.backend.sqlitedb import SDB


class PlanetSchematic(object):

    SQL = [
            'SELECT typeID, quantity from planetSchematicsTypeMap WHERE isInput = 1 AND schematicID = %s',
            'SELECT typeID, quantity from planetSchematicsTypeMap WHERE isInput = 0 AND schematicID = %s'           
           ]


    def __init__(self, assets, data):
        self.assets         = assets
        self.uid            = data[0]
        self.name           = data[1]
        self.cycleTime      = data[2]

        self._input         = None      
        self._output        = None


    @property
    def input(self):
        if self._input is None:
            self._input = []
            for entry in SDB.queryAll(PlanetSchematic.SQL[0] % self.uid):
                self._input.append((self.assets.type[entry[0]], int(entry[1])))
        return self._input
    
    
    @property
    def output(self):
        if self._output is None:
            self._output = []
            for entry in SDB.queryAll(PlanetSchematic.SQL[1] % self.uid):
                self._output.append((self.assets.type[entry[0]], int(entry[1])))
        return self._output
