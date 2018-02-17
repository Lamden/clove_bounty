from clove.network.bitcoin import Bitcoin


class Garlicoin(Bitcoin):
    """
    Class with all the necessary Garlicoin (GRLC) network information based on
    https://github.com/GarlicoinOrg/Garlicoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'garlicoin'
    symbols = ('GRLC', )
    seeds = ('dnsseed.brennanmcdonald.io', 'dnsseed.rshaw.space')
    port = 42069


class GarlicoinTestNet(Garlicoin):
    """
    Class with all the necessary Garlicoin (GRLC) testing network information based on
    https://github.com/GarlicoinOrg/Garlicoin/blob/master/src/chainparams.cpp    
    (date of access: 02/16/2018)
    """
    name = 'test-garlicoin'
    seeds = ('dnsseed-testnet.brennanmcdonald.io', 'dnsseed-testnet.rshaw.space')
    port = 42075
