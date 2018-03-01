from clove.network.bitcoin import Bitcoin


class Infinitecoin(Bitcoin):
    """
    Class with all the necessary Infinitecoin network information based on
    https://github.com/infinitecoin/infinitecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'infinitecoin'
    symbols = ('IFC', )
    seeds = ("dnsseed.infinitecoinpool.org",
             "dnsseed.bytesized-vps.com",
             "dnsseed.ltc.xurious.com")
    port = 9321
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 230
    }
