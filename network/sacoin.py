from clove.network.bitcoin import Bitcoin


class SACoin(Bitcoin):
    """
    Class with all the necessary SACoin (SAC) network information based on
    https://github.com/sacoin/Sacoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'sacoin'
    symbols = ('SAC', )
    seeds = ('seed5.cryptolife.net', 'seed2.cryptolife.net', 'seed3.cryptolife.net', 'electrum1.cryptolife.net',
             'wallet.cryptolife.net', 'explore.cryptolife.net')
    port = 21996

# no testnet
