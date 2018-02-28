from clove.network.bitcoin import Bitcoin


class Levocoin(Bitcoin):
    """
    Class with all the necessary Levocoin (LEVO) network information based on
    https://github.com/levoserve/levocoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'levocoin'
    symbols = ('LEVO', )
    seeds = ('162.243.28.171',
             '162.243.113.23',
             'seed1.cryptolife.net',
             'seed2.cryptolife.net',
             'seed3.cryptolife.net',
             'electrum3.cryptolife.net',
             'wallet.cryptolife.net',
             'explore.cryptolife.net')
    port = 17655

# no testnet
