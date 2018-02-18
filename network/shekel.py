from clove.network.bitcoin import Bitcoin


class Shekel(Bitcoin):
    """
    Class with all the necessary Shekel (JEW) network information based on
    https://github.com/shekeltechnologies/JewNew/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'shekel'
    symbols = ('JEW', )
    seeds = ('nodes.shekel.pw', 'shekel.nodes.gyservers.com', '209.250.241.176', '209.250.243.131', '45.77.239.108',
			 '107.191.44.102', '199.247.6.191', '45.77.9.77', '45.77.62.126', '108.61.96.146')
    port = 5500


class ShekelTestNet(Shekel):
    """
    Class with all the necessary Shekel (JEW) testing network information based on
    https://github.com/shekeltechnologies/JewNew/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-shekel'
    seeds = ('207.148.0.129', '45.77.239.30', '45.76.226.204')
    port = 51434
