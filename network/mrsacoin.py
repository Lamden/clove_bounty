from clove.network.bitcoin import Bitcoin


class MrsaCoin(Bitcoin):
    """
    Class with all the necessary MrsaCoin network information based on
    https://github.com/mrsacoin/mrsacoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'mrsacoin'
    symbols = ('MRSA', )
    seeds = ("45.42.140.50")
    port = 17930
    message_start = b'\xc3\xc1\xfa\xfc'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 77,
        'SECRET_KEY': 178
    }

# no testnet
