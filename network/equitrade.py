from clove.network.bitcoin import Bitcoin


class Equitrade(Bitcoin):
    """
    Class with all the necessary Equitrade network information based on
    https://github.com/equitrader/equitrade/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'equitrade'
    symbols = ('EQT', )
    seeds = ("seed1.cryptolife.net", "seed2.cryptolife.net", "seed3.cryptolife.net",
             "seed5.cryptolife.net", "wallet.cryptolife.net", "explore.cryptolife.net")
    port = 43103


# Equitrade has no Testnet
