from clove.network.bitcoin import Bitcoin


class Allsafe(Bitcoin):
    """
    Class with all the necessary Photon network information based on
    https://github.com/securitybank/allsafe2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'allsafe'
    symbols = ('ASAFE2', )
    nodes = ("63.142.254.223", )
    port = 30234
    message_start = b'\x32\x5e\x6f\x86'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }

# Has no testnet
