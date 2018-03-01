from clove.network.bitcoin import Bitcoin


class Frazcoin(Bitcoin):
    """
    Class with all the necessary Frazcoin network information based on
    https://github.com/frazcoin/frazCoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'frazcoin'
    symbols = ('FRAZ', )
    seeds = ("frazcoin.eu")
    port = 3991


class FrazcoinTestNet(Frazcoin):
    """
    Class with all the necessary Frazcoin testing network information based on
    https://github.com/frazcoin/frazCoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-frazcoin'
    seeds = ("frazcoin.eu")
    port = 3981
