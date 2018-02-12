from clove.network.bitcoin import Bitcoin


class Toacoin(Bitcoin):
    """
    Class with all the necessary TOA network information based on
    https://github.com/toacoin/toa/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'toacoin'
    symbols = ('TOA', )
    seeds = (
        '212.24.111.232',
        '212.24.111.8',
        '212.24.111.34',
    )
    port = 9642


class ToacoinTestNet(Toacoin):
    """
    Class with all the necessary TOA testing network information based on
    https://github.com/toacoin/toa/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-toacoin'
    seeds = ()
    port = 19642
