from clove.network.bitcoin import Bitcoin


class XCash(Bitcoin):
    """
    Class with all the necessary XCash network information based on
    https://github.com/JohnnyXCash/XCash/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xcash'
    symbols = ('XCASH', )
    seeds = ("seed.xcash.cc", )
    port = 32524
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 203
    }

# no testnet
