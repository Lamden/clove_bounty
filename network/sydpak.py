from clove.network.bitcoin import Bitcoin


class SydPak(Bitcoin):
    """
    Class with all the necessary SydPak network information based on
    https://github.com/stewpak/Sydpak/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sydpak'
    symbols = ('SDP', )
    nodes = ("89.204.139.80", )
    port = 54321
    message_start = b'\x5a\xc3\x82\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }

# no testnet
