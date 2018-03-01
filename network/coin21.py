from clove.network.bitcoin import Bitcoin


class Coin21(Bitcoin):
    """
    Class with all the necessary Coin2.1 (C2) network information based on
    https://github.com/UdjinM6/Coin2.1/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'coin21'
    symbols = ('C2', )
    seeds = ('107.181.166.143', '24.22.50.162')
    port = 22222
    message_start = b'\xce\xfb\xfa\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 156
    }

# no testnet
