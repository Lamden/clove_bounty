from clove.network.bitcoin import Bitcoin


class Forexcoin(Bitcoin):
    """
    Class with all the necessary Forexcoin network information based on
    https://github.com/forexcoin/forexcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'forexcoin'
    symbols = ('FRX', )
    seeds = ("v3dnsseed.globalforexcoin.com")
    port = 9369
    message_start = b'\xf6\xe6\xd6\xc6'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 163
    }


class ForexcoinTestNet(Forexcoin):
    """
    Class with all the necessary Forexcoin testing network information based on
    https://github.com/forexcoin/forexcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-forexcoin'
    seeds = ("v3testnet-seed.globalforexcoin.com")
    port = 19369
    message_start = b'\xf2\xe2\xbd\xc7'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
