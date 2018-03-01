from clove.network.bitcoin import Bitcoin


class Blakecoin(Bitcoin):
    """
    Class with all the necessary Blakecoin network information based on
    https://github.com/BlueDragon747/Blakecoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'blakecoin'
    symbols = ('BLC', )
    seeds = ("blakecoin.org",
             "blakecoin.com")
    port = 8773
    message_start = b'\xf9\xbe\xb4\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 7,
        'SECRET_KEY': 154
    }


class BlakecoinTestNet(Blakecoin):
    """
    Class with all the necessary Blakecoin testing network information based on
    https://github.com/BlueDragon747/Blakecoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-blakecoin'
    seeds = ("blakecoin.org",
             "blakecoin.com")
    port = 18773
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 142,
        'SCRIPT_ADDR': 170,
        'SECRET_KEY': 270
    }
