
from clove.network.bitcoin import Bitcoin


class Cerium(Bitcoin):
    """
    Class with all the necessary Cerium network information based on
    https://github.com/ceriumdev/cerium/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cerium'
    symbols = ('XCE', )
    seeds = ("104.131.117.31")
    port = 45455
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }

# Has no testnet
