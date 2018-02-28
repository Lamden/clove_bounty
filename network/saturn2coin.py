from clove.network.bitcoin import Bitcoin


class Saturn2Coin(Bitcoin):
    """
    Class with all the necessary Saturn2Coin network information based on
    https://github.com/Flapmin/SAT2/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'saturn2coin'
    symbols = ('SAT2', )
    seeds = ("seed.saturn2coin.mycryptocoins.net",
             "seednodes.saturn2coin.mycryptocoins.net")
    port = 17771

# no testnet
