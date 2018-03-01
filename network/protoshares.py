from clove.network.bitcoin import Bitcoin


class Protoshares(Bitcoin):
    """
    Class with all the necessary Protoshares network information based on
    https://github.com/BrownBear2/ProtoShares/blob/psforkinit/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'protoshares'
    symbols = ('PTS*', )
    seeds = ("162.243.45.158",
             "192.241.150.158",
             "162.243.67.4",
             "162.243.54.126",
             "37.139.29.236",
             "64.90.183.137",
             "111.93.163.251",
             "54.219.164.96",
             "198.211.112.13",
             "50.112.199.32",
             "106.187.41.67",
             "54.218.232.206",
             "54.212.175.33")
    port = 3888
    message_start = b'\xf9\xbd\xb5\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 56,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 184
    }


class ProtosharesTestNet(Protoshares):
    """
    Class with all the necessary Protoshares testing network information based on
    https://github.com/BrownBear2/ProtoShares/blob/psforkinit/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-protoshares'
    seeds = ("testnet-seed.bitcoin.petertodd.org",
             "testnet-seed.bluematt.me")
    port = 13888
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
