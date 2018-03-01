from clove.network.bitcoin import Bitcoin


class Goacoin(Bitcoin):
    """
    Class with all the necessary Goacoin network information based on
    https://github.com/goacoincore/goacoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'goacoin'
    symbols = ('GOA', )
    seeds = ("seed1.goaco.in",
             "seed2.goaco.in",
             "seed3.goaco.in",
             "seed4.goaco.in")
    port = 1947
    message_start = b'\xa2\xc4\xcb\x4a'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 198
    }

# no testnet
