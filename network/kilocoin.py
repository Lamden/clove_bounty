from clove.network.bitcoin import Bitcoin


class Kilocoin(Bitcoin):
    """
    Class with all the necessary Kilocoin (KLC) network information based on
    https://github.com/kilocoin/kilocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'kilocoin'
    symbols = ('KLC', )
    seeds = ('dnsseed.kilocoin.com')
    port = 3112


class KilocoinTestNet(Kilocoin):
    """
    Class with all the necessary Kilocoin (KLC) testing network information based on
    https://github.com/kilocoin/kilocoin/blob/master/src/net.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-kilocoin'
    seeds = ('testnet-seed.kilocoin.com')
    port = 63112
