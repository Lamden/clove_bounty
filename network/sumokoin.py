from clove.network.bitcoin import Bitcoin


class Sumokoin(Bitcoin):
    """
    Class with all the necessary Sumokoin (SUMO) network information based on
    https://github.com/sumoprojects/sumokoin/blob/master/src/p2p/net_node.inl
    (date of access: 02/22/2018)
    """
    name = 'sumokoin'
    symbols = ('SUMO', )
    seeds = ('158.69.242.193',
             '91.121.81.92',
             '144.217.164.165',
             '168.235.77.153',
             '185.34.136.245',
             '107.191.61.96')
    port = 19733


class SumokoinTestNet(Sumokoin):
    """
    Class with all the necessary Sumokoin (SUMO) testing network information based on
    https://github.com/sumoprojects/sumokoin/blob/master/src/p2p/net_node.inl
    (date of access: 02/22/2018)
    """
    name = 'test-sumokoin'
    seeds = ('158.69.242.193',
             '91.121.81.92',
             '144.217.164.165')
    port = 29733
