from clove.network.bitcoin import Bitcoin


class NodeCoin(Bitcoin):
    """
    Class with all the necessary NodeCoin network information based on
    https://github.com/nodecoins/sources/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'nodecoin'
    symbols = ('NODC', )
    seeds = ('212.8.251.4')
    port = 9219


# Has no testnet
