from clove.network.bitcoin import Bitcoin


class GeoCoin(Bitcoin):
    """
    Class with all the necessary GeoCoin network information based on
    https://github.com/onetimer/onetimer/blob/master/src/net.cpp
    (date of access: 02/22/2018)
    """
    name = 'geocoin'
    symbols = ('GEO', )
    seeds = ("104.236.52.122")
    port = 9748


class GeoCoinTestNet(GeoCoin):
    """
    Class with all the necessary GeoCoin testing network information based on
    https://github.com/onetimer/onetimer/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-geocoin'
    seeds = ("104.236.52.122")
    port = 9748
