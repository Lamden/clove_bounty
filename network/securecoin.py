
from clove.network.bitcoin import Bitcoin


class SecureCoin(Bitcoin):
    """
    Class with all the necessary SRC network information based on
    http://www.github.com/securecoin/Securecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'securecoin'
    symbols = ('SRC', )
    seeds = ('securecoin.org', )
    port = 12567
    message_start = b'\xfc\xb4\xd9\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 125,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 253
    }
