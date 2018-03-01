from clove.network.bitcoin import Bitcoin


class Dreamcoin(Bitcoin):
    """
    Class with all the necessary Dreamcoin (DRM) network information based on
    https://github.com/tsosunov/Dreamcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'dreamcoin'
    symbols = ('DRM', )
    seeds = ('seed1.cryptolife.net', 'seed2.cryptolife.net', )
    port = 16783
    message_start = b'\xf1\xe0\xa2\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
