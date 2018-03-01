from clove.network.bitcoin import Bitcoin


class Maza(Bitcoin):
    """
    Class with all the necessary Maza network information based on
    https://github.com/MazaCoin/MazaCoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'maza'
    symbols = ('MZC', )
    seeds = ("node.mazacoin.org",
             "node.mazacoin.cf",
             "mazacoin.no-ip.org")
    port = 12835

# no testnet
