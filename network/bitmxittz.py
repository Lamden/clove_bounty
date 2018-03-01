from clove.network.bitcoin import Bitcoin


class Bitmxittz(Bitcoin):
    """
    Class with all the necessary Bitmxittz network information based on
    https://github.com/bitmxittz/Bitmxittz/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitmxittz'
    symbols = ('BMXT', )
    seeds = ("52.192.16.19")
    port = 14433
    message_start = b'\xc2\xd1\xd3\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 153
    }


class BitmxittzTestNet(Bitmxittz):
    """
    Class with all the necessary Bitmxittz testing network information based on
    https://github.com/bitmxittz/Bitmxittz/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-bitmxittz'
    seeds = ("testnet-seed.bitmxittztools.com",
             "testnet-seed.ltc.xurious.com",
             "dnsseed.wemine-testnet.com")
    port = 15433
    message_start = b'\xd9\xb6\xa3\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
