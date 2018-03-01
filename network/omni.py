from clove.network.bitcoin import Bitcoin


class Omni(Bitcoin):
    """
    Class with all the necessary Omni network information based on
    https://github.com/mastercoin-MSC/mastercore/blob/mscore-0.0.9/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'omni'
    symbols = ('OMNI', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "seed.bitcoinstats.com",
             "seed.bitnodes.io",
             "bitseed.xf2.org")
    port = 8333
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class OmniTestNet(Omni):
    """
    Class with all the necessary Omni testing network information based on
    https://github.com/mastercoin-MSC/mastercore/blob/mscore-0.0.9/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-omni'
    seeds = ("testnet-seed.bitcoin.petertodd.org", "testnet-seed.bluematt.me")
    port = 18333
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
