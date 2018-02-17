from clove.network.bitcoin import Bitcoin


class Startcoin(Bitcoin):
    """
    Class with all the necessary Startcoin (START) network information based on
    https://github.com/startcoin-project/startcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'startcoin'
    symbols = ('START', )
    seeds = ('node1.startcoin.org', 'node2.startcoin.org')
    port = 9247

# no testnet
