

class Stream:
    def __init__(self, src, label, typ):
        self.src = src
        self.label = label
        self.type = typ

    def __str__(self):
        return "label:{},src:{}".format(self.label, self.src)
