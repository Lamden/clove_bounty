from clove.network.bitcoin import Bitcoin


class Gambit(Bitcoin):
    """
    Class with all the necessary Gambit (GAM) network information based on
    https://github.com/collincrypto/gambitcrypto/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'gambit'
    symbols = ('GAM', )
    seeds = ('node1.gambitcrypto.com', 'node2.gambitcrypto.com', 'node3.gambitcrypto.com')
    port = 47077

# no testnet
