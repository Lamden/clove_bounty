from clove.network.bitcoin import Bitcoin


class AnalCoin(Bitcoin):
    """
    Class with all the necessary AnalCoin network information based on
    https://github.com/analcoin/analcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'analcoin'
    symbols = ('ANAL', )
    seeds = ("108.61.178.105")
    port = 4669


# Has no testnet
