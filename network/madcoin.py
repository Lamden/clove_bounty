from clove.network.bitcoin import Bitcoin


class Madcoin(Bitcoin):
    """
    Class with all the necessary Madcoin network information based on
    https://github.com/madcoin-project/madcoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'madcoin'
    symbols = ('MDC', )
    seeds = ("block.madcoin.life",
             "node1.madcoin.life",
             "node2.madcoin.life")
    port = 10882

# no testnet
