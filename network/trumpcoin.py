from clove.network.bitcoin import Bitcoin


class Trumpcoin(Bitcoin):
    """
    Class with all the necessary Trumpcoin (TRUMP) network information based on
    https://github.com/TRUMPCOIN/TRUMP/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'trumpcoin'
    symbols = ('TRUMP', )
    seeds = ('173.44.41.235', '178.33.84.2')
    port = 8468


class TrumpcoinTestNet(Trumpcoin):
    """
    Class with all the necessary Trumpcoin (TRUMP) testing network information based on
    https://github.com/TRUMPCOIN/TRUMP/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-trumpcoin'
    seeds = ('173.44.41.235', )
    port = 18468
