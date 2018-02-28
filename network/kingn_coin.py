from clove.network.bitcoin import Bitcoin


class KingNCoin(Bitcoin):
    """
    Class with all the necessary KingN Coin network information based on
    https://github.com/ulandort/kingncoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'kingncoin'
    symbols = ('KNC', )
    seeds = ("node.walletbuilders.com")
    port = 18373


# Has no testnet
