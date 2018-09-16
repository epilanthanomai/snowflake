from collections import defaultdict

class cell(defaultdict):
    def __init__(self):
        defaultdict.__init__(self, float)
