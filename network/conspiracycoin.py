from clove.network.bitcoin import Bitcoin


class conspiracycoin(Bitcoin):
    """
    Class with all the necessary Conspiracycoin network information based on
    https://github.com/C-Y-Coin/cyc-master/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'conspiracycoin'
    symbols = ('CYC', )
    seeds = ("seeder1.conspiracycoin.org",
             "seeder2.conspiracycoin.org",
             "seeder3.conspiracycoin.org",
             "seeder4.conspiracycoin.org",
             "seeder5.conspiracycoin.org",
             "seeder6.conspiracycoin.org",
             "seeder7.conspiracycoin.org")
    port = 33834
