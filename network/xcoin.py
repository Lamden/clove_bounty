from clove.network.bitcoin import Bitcoin


class XCoin(Bitcoin):
    """
    Class with all the necessary XCoin network information based on
    https://github.com/jimblasko/xcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'x-coin'
    symbols = ('XCO', )
    nodes = ("198.105.125.193", "198.105.125.194", "198.105.122.152", )
    port = 14641
    message_start = b'\xa5\xd2\xd7\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 203
    }
