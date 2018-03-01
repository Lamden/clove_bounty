from clove.network.bitcoin import Bitcoin


class BitQuark(Bitcoin):
    """
    Class with all the necessary BitQuark (BTQ) network information based on
    https://github.com/bitquarkcoin/BitQuark/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'bitquark'
    symbols = ('BTQ', )
    seeds = ('62.210.125.140', '107.170.17.20', '85.25.195.74',
             '217.23.10.247', '62.210.178.237', '128.2.209.18')
    port = 9596
    message_start = b'\xfe\xa5\x03\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 128
    }

# no testnet
