from clove.network.bitcoin import Bitcoin


class Wmcoin(Bitcoin):
    """
    Class with all the necessary WMC network information based on
    https://github.com/wemcoin/wmcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'wmcoin'
    symbols = ('WMC', )
    seeds = (
        '120.27.114.125',
    )
    port = 32866


class WmcoinTestNet(Wmcoin):
    """
    Class with all the necessary WMC testing network information based on
    https://github.com/wemcoin/wmcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-wmcoin'
    seeds = ()
    port = 30801
