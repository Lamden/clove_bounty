from clove.network.bitcoin import Bitcoin


class Furrycoin(Bitcoin):
    """
    Class with all the necessary Furrycoin network information based on
    https://github.com/prolifik/Furrycoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'furrycoin'
    symbols = ('FUR', )
    seeds = ("seed1.furrycoin.net", )
    port = 11000
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }


class FurrycoinTestNet(Furrycoin):
    """
    Class with all the necessary Furrycoin testing network information based on
    https://github.com/prolifik/Furrycoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'test-furrycoin'
    seeds = ("test-seed1.furrycoin.net", )
    port = 5744
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
