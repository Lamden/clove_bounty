from clove.network.bitcoin import Bitcoin


class Murraycoin(Bitcoin):
    """
    Class with all the necessary Murraycoin network information based on
    https://github.com/murraycoin/murraycoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'murraycoin'
    symbols = ('MRY', )
    seeds = ("dnsseed1.murraycoin.org",
             "dnsseed2.murraycoin.org",
             "sfo.fusionhash.com")
    port = 11951
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }

# no testnet
