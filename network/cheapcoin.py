from clove.network.bitcoin import Bitcoin


class Cheapcoin(Bitcoin):
    """
    Class with all the necessary Cheapcoin (CHEAP) network information based on
    https://github.com/cheapandcloud/chain/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'cheapcoin'
    symbols = ('CHEAP', )
    seeds = ('54.70.9.148')
    port = 36648

# no testnet
