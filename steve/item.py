

class Item(object):


    def __init__(self, assets, data):
        self.assets         = assets
        self.uid            = data[0]
        self.typeID         = data[1]
        self.ownerID        = data[2]
        self.locationID     = data[3]
        self.flagID         = data[4]
        self.quantity       = data[5]
        self.singleton      = data[6]


    @property
    def type(self):
        return self.assets.type[self.typeID]
    
    
    @property
    def containedIn(self):
        return self.assets.inventoryFlag[self.flagID]