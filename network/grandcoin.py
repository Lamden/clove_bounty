from clove.network.bitcoin import Bitcoin


class GrandCoin(Bitcoin):
    """
    Class with all the necessary GrandCoin network information based on
    https://github.com/grandcoingdc/grandcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'grandcoin'
    symbols = ('GDC', )
    seeds = ("dnsseed.grandcoinpool.org",
             "dnsseed.bytesized-vps.com", "dnsseed.ltc.xurious.com")
    port = 12377
