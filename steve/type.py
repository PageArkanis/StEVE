from steve.backend.sqlitedb import SDB


class Type(object):

    SQL = [
           'SELECT * from invMetaTypes             WHERE typeID = %s',
           'SELECT * from invTypeMaterials         WHERE typeID = %s',
           'SELECT * from industryActivityProducts WHERE productTypeID = %s',
           ]

    def __init__(self, assets, data):
        self.assets         = assets
        
        # copy constructor part
        if isinstance(data, Type):
            data = data.data

        self.uid            = data[0]
        self.groupID        = data[1]
        self.name           = data[2]
        self.description    = data[3]
        self.mass           = data[4]
        self.volume         = data[5]
        self.capacity       = data[6]
        self.portionSize    = data[7]
        self.raceID         = data[8]
        self.basePrice      = data[9]
        self.published      = data[10]
        self.marketGroupID  = data[11]
        self.iconID         = data[12]
        self.soundID        = data[13]
        self.graphicID      = data[14]

        self._metaType      = None
        self._hasBPO        = None
        self._bpo           = None
    

    @property
    def data(self):
        return [self.uid,    self.groupID,   self.name,      self.description,
                self.mass,   self.volume,    self.capacity,  self.portionSize,
                self.raceID, self.basePrice, self.published, self.marketGroupID,
                self.iconID, self.soundID,   self.graphicID]


    @property
    def marketGroup(self):
        if self.marketGroupID:
            return self.assets.marketGroup[self.marketGroupID]


    @property
    def metaType(self):
        if self._metaType is None:
            result = SDB.queryOne(Type.SQL[0] % self.uid)
            if result:
                self._parentTypeID = result[1]
                self._metaType     = result[2]
            else:
                self._parentTypeID = 0
                self._metaType     = 0
        return self._metaType


    @property
    def parentTypeID(self):
        if self._parentTypeID is None:
            result = SDB.queryOne(Type.SQL[0] % self.uid)
            if result:
                self._parentTypeID = result[1]
                self._metaType     = result[2]
            else:
                self._parentTypeID = 0
                self._metaType     = 0
                
        return self._parentTypeID


    @property
    def parentType(self):
        if self.parentTypeID:
            return self.assets.type[self.parentTypeID]


    @property
    def hasBPO(self):
        if self._hasBPO is None:
            result       = SDB.queryOne(Type.SQL[2] % self.uid)
            self._hasBPO = result and result[1] == 1
            if self._hasBPO:
                self._bpo = self.assets.blueprint.get(result[0])

        return self._hasBPO
    

    @property
    def isBPO(self):
        return self.uid in self.assets.blueprint

    
    @property
    def bpo(self):

        if self.isBPO:
            return self
        
        if self.hasBPO:
            return self._bpo
        

    @property
    def bom(self):
        result = []
        for entry in SDB.queryAll(Type.SQL[1] % self.uid):
            result.append( (self.assets.type[entry[1]], entry[2]) )
        return result
