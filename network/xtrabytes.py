from clove.network.bitcoin import Bitcoin


class Xtrabytes(Bitcoin):
    """
    Class with all the necessary Xtrabytes network information based on
    https://github.com/borzalom/xtrabytes/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Xtrabytes'
    symbols = ('XBY', )
    seeds = ("79.172.210.27", "79.172.210.45")
    port = 34002


# Has no Testnet
