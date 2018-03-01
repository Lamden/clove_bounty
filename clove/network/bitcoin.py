class Bitcoin(object):

    blacklist_nodes = {}

    @property
    def default_symbol(self):
        return self.symbols[0]
