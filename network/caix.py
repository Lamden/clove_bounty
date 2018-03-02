from clove.network.bitcoin import Bitcoin


class CAIx(Bitcoin):
    """
    Class with all the necessary CAIx network information based on
    https://github.com/Lefter1s/CAIx/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'CAIx'
    symbols = ('CAIx', )
    seeds = ("walrusbonzo.ddns.net",
             "alpho2k.ddns.net")
    port = 1511
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 76,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 204
    }

# Has no testnet
