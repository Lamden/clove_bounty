from clove.network.bitcoin import Bitcoin


class Eryllium(Bitcoin):
    """
    Class with all the necessary Eryllium (ERY) network information based on
    https://github.com/Eryllium/project/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'eryllium'
    symbols = ('ERY', )
    seeds = ('138.197.23.193', 'seed1.cryptolife.net', 'seed2.cryptolife.net',
             'seed3.cryptolife.net', 'electrum1.cryptolife.net', 'explore.cryptolife.net')
    port = 34821

# no testnet
