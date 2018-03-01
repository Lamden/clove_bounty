from clove.network.bitcoin import Bitcoin


class Copperlark(Bitcoin):
    """
    Class with all the necessary Copperlark network information based on
    https://github.com/copperlark/clr/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'copperlark'
    symbols = ('CLR', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "bitseed.xf2.org")
    port = 10333
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class CopperlarkTestNet(Copperlark):
    """
    Class with all the necessary Copperlark testing network information based on
    https://github.com/copperlark/clr/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-copperlark'
    seeds = ("testnet-seed.bitcoin.petertodd.org")
    port = 20333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
