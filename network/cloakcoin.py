from clove.network.bitcoin import Bitcoin


class CloakCoin(Bitcoin):
    """
    Class with all the necessary CloakCoin network information based on
    https://github.com/CloakCoin/CloakCoinRelaunch/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cloakcoin'
    symbols = ('CLOAK', )
    seeds = ("cloakseed.getsuperconductor.com")
    port = 29662
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 27,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 155
    }

# Has no testnet
