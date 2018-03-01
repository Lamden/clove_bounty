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
    message_start = b'\xb4\xf4\xe6\xe8'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 191
    }

# no testnet
