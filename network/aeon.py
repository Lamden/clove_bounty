from clove.network.bitcoin import Bitcoin


class Aeon(Bitcoin):
    """
    Class with all the necessary Aeon (AEON) network information based on
    https://github.com/aeonix/aeon/blob/master/src/p2p/net_node.inl
    (date of access: 02/22/2018)
    """
    name = 'aeon'
    symbols = ('AEON', )
    nodes = ('74.91.23.186', '192.187.114.114', )
    port = 11180

# no testnet
