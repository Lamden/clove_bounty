from clove.network.bitcoin import Bitcoin


class Gram_Coin(Bitcoin):
    """
    Class with all the necessary Gram Coin network information based on
    https://github.com/kilogram1/kilogram1/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'gram_coin'
    symbols = ('GRAM', )
    seeds = ("node.GramCoin.org",
             "node.GramCoin.cf",
             "GramCoin.no-ip.org")
    port = 7567

# no testnet
