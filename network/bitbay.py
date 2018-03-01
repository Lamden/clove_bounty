from clove.network.bitcoin import Bitcoin


class BitBay(Bitcoin):
    """
    Class with all the necessary BitBay network information based on
    https://github.com/bitbayteam/bitbay/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitbay'
    symbols = ('BAY', )
    nodes = ("178.62.201.53", "128.199.251.218", )
    port = 19914
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# Has no testnet
