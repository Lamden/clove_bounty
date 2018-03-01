from clove.network.bitcoin import Bitcoin


class BitSoar(Bitcoin):
    """
    Class with all the necessary BitSoar (BSR) network information based on
    https://github.com/BITSOAR/wallet/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'bitsoar'
    symbols = ('BSR', )
    nodes = ('139.59.7.111', '138.197.156.193', )
    port = 40119
    message_start = b'\x53\x74\x69\x42'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 154
    }

# no testnet
