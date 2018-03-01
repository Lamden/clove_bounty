from clove.network.bitcoin import Bitcoin


class Aseancoin(Bitcoin):
    """
    Class with all the necessary Aseancoin network information based on
    https://github.com/tyemday/Aseancoin/blob/master/src/chainparams/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'aseancoin'
    symbols = ('ASN', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "seed.bitcoinstats.com",
             "bitseed.xf2.org")
    port = 8333
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class AseancoinTestNet(Aseancoin):
    """
    Class with all the necessary Aseancoin testing network information based on
    https://github.com/tyemday/Aseancoin/blob/master/src/chainparams/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-aseancoin'
    seeds = ("testnet-seed.alexykot.me",
             "testnet-seed.bitcoin.petertodd.org",
             "testnet-seed.bluematt.me",
             "testnet-seed.bitcoin.schildbach.de")
    port = 18333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
