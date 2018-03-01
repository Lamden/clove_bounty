from clove.network.bitcoin import Bitcoin


class FreeGameZone(Bitcoin):
    """
    Class with all the necessary Free Game Zone network information based on
    https://github.com/carlcaleb43/freegamezone-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'free_game_zone'
    symbols = ('FGZ', )
    nodes = ("45.32.217.42", )
    port = 8999
    message_start = b'\x3d\x09\x06\x43'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 163
    }

# no testnet
