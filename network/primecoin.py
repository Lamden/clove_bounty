from clove.network.bitcoin import Bitcoin


class Primecoin(Bitcoin):
    """
    Class with all the necessary Primecoin network information based on
    https://github.com/primecoin/primecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'primecoin'
    symbols = ('XPM', )
    seeds = (
        'seed.ppcoin.net',
        'dnsseed.xpm.altcointech.net',
        'dnsseed.xpm2.altcointech.net',
        'primeseed.muuttuja.org'
    )
    port = 9911


class PrimecoinTestNet(Primecoin):
    """
    Class with all the necessary Primecoin testing network information based on
    https://github.com/primecoin/primecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-primecoin'
    seeds = (
        'tnseed.ppcoin.net', 'primeseedtn.muuttuja.org'
    )
    port = 9913
