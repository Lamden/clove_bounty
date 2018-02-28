from clove.network.bitcoin import Bitcoin


class BritCoin(Bitcoin):
    """
    Class with all the necessary BritCoin network information based on
    https://github.com/Brit-Coin/britcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'britcoin'
    symbols = ('BRIT', )
    seeds = ("1.britcoin.io",
             "2.britcoin.io")
    port = 9197

# Has no testnet
