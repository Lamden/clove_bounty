from clove.network.bitcoin import Bitcoin


class Swing(Bitcoin):
    """
    Class with all the necessary Swing network information based on
    https://github.com/swingcoin/swing/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'swing'
    symbols = ('SWING', )
    seeds = ("104.236.29.198","swing.suprnova.cc")
    port = 16061


# Has no testnet