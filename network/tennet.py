from clove.network.bitcoin import Bitcoin


class TenneT(Bitcoin):
    """
    Class with all the necessary TenneT network information based on
    https://github.com/TenneTCo/TenneT/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'tennet'
    symbols = ('TENNET', )
    seeds = ("52.26.15.236")
    port = 9782
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 41,
        'SCRIPT_ADDR': 7,
        'SECRET_KEY': 169
    }

# no testnet
