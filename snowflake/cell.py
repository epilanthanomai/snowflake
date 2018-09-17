from collections import defaultdict

class hex_state(defaultdict):
    """hexagonal cellular automaton state

    Arrangement:
               -1,0
         0,-1         -1,+1
                0,0
        +1,-1          0,+1
               +1,0
    """

    NEIGHBORS = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

    def __init__(self, *items, **kwargs):
        default = kwargs.pop('default', 0)
        default_factory = kwargs.pop('default_factory', lambda: default)
        defaultdict.__init__(self, default_factory, *items, **kwargs)

    def _copy(self, items):
        return hex_state(
                ((k, v)
                 for (k, v) in items),
                default_factory=self.default_factory)

    def neighboring_values(self, x, y):
        return (self[x+a, y+b] for (a,b) in self.NEIGHBORS)

    def map(self, f):
        return self._copy(
                ((k, f(v))
                 for (k, v) in self.items()))

    def map_with_neighbors(self, f):
        # collect the items and then iterate them, to avoid a case where
        # calculating neighboring_values creates new items while we're
        # iterating
        items = list(self.items())
        return self._copy(
                ((k, f(v, self.neighboring_values(*k)))
                 for (k, v) in items))
