from clove.network.bitcoin import Bitcoin


class Golfcoin(Bitcoin):
    """
    Class with all the necessary Golfcoin (GOLF) network information based on
    https://github.com/Golfcoin/2.0/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'golfcoin'
    symbols = ('GOLF', )
    seeds = ('seed1.cryptolife.net',
             'seed2.cryptolife.net',
             'seed3.cryptolife.net',
             'electrum1.cryptolife.net',
             'electrum3.cryptolife.net',
             'explore.cryptolife.net')
    port = 38931

# no testnet
