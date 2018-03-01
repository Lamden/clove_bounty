from clove.network.bitcoin import Bitcoin


class Latium(Bitcoin):
    """
    Class with all the necessary Latium network information based on
    https://github.com/LatiumCoin/Latium/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'latium'
    symbols = ('LAT', )
    seeds = ("seed1.latium.cc",
             "seed2.latium.cc",
             "seed3.latium.cc")
    port = 12688
    message_start = b'\xae\xdb\xfc\xb2'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 83,
        'SECRET_KEY': 151
    }
