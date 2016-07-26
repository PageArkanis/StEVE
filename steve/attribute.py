

class Attribute(object):


    def __init__(self, assets, data):
        self.assets             = assets
        self.uid                = data[0]
        self.name               = data[1]
        self.description        = data[2]
        self.iconID             = data[3]
        self.shortDescription   = data[4]
        self.notes              = data[5]


