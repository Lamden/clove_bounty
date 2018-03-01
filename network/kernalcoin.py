from clove.network.bitcoin import Bitcoin


class Kernalcoin(Bitcoin):
    """
    Class with all the necessary Kernalcoin network information based on
    https://github.com/kernalcoin/Kernal/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kernalcoin'
    symbols = ('KC', )
    seeds = ("45.63.71.91")
    port = 4769

# no testnet
