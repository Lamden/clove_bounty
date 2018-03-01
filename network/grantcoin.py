from clove.network.bitcoin import Bitcoin


class Grantcoin(Bitcoin):
    """
    Class with all the necessary Grantcoin network information based on
    https://github.com/grantcoin/grantcoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'grantcoin'
    symbols = ('GRT', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "bitseed.xf2.org")
    port = 8333
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }

# no testnet
