

class Race(object):


    def __init__(self, assets, data):
        self.assets             = assets
        self.uid                = data[0]
        self.name               = data[1]
        self.description        = data[2]
        self.shortDescription   = data[3]

