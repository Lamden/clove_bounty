from clove.network.bitcoin import Bitcoin


class Articcoin(Bitcoin):
    """
    Class with all the necessary Articcoin (ARC) network information based on
    https://github.com/ArcticCore/arcticcoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'articcoin'
    symbols = ('ARC', )
    nodes = ('5.9.65.168', '5.9.55.201', '78.46.75.49', '78.47.238.36')
    port = 7209


class ArticcoinTestNet(Articcoin):
    """
    Class with all the necessary Articcoin (ARC) testing network information based on
    https://github.com/ArcticCore/arcticcoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-articcoin'
    nodes = ('5.9.65.168', '5.9.55.201', '78.46.75.49', '78.47.238.36')
    port = 17209
