from clove.network.bitcoin import Bitcoin


class Roofs(Bitcoin):
    """
    Class with all the necessary  Roofs (ROOFS) network information based on
    https://github.com/roofsdev/roofs/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'roofs'
    symbols = ('ROOFS', )
    nodes = ('192.161.48.19', )
    port = 20019
    message_start = b'\x90\x4a\x92\x40'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 188
    }


# no testnet
