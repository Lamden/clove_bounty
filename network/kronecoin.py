from clove.network.bitcoin import Bitcoin


class Kronecoin(Bitcoin):
    """
    Class with all the necessary Kronecoin network information based on
    https://github.com/Kronecoin/Kronecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kronecoin'
    symbols = ('KRONE', )
    seeds = ("35.176.102.26",
             "35.176.12.96",
             "35.176.130.60",
             "35.176.166.149",
             "seed.kronecoin.org")
    port = 16765
