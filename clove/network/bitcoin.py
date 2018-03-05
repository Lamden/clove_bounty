class Bitcoin(object):

    seeds = ()
    nodes = ()
    blacklist_nodes = {}

    @property
    def default_symbol(self):
        return self.symbols[0]
