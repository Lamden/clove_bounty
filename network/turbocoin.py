from clove.network.bitcoin import Bitcoin


class TurboCoin(Bitcoin):
    """
    Class with all the necessary TurboCoin (TURBO) network information based on
    https://github.com/TurboCoinProject/TurboCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'turbocoin'
    symbols = ('TURBO', )
    nodes = ('195.181.245.38', )
    port = 35282
    message_start = b'\xa4\xb1\xf3\xc2'
    base58_prefixes = {
        'PUBKEY_ADDR': 127,
        'SCRIPT_ADDR': 24,
        'SECRET_KEY': 255
    }

# no testnet
