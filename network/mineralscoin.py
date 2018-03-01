from clove.network.bitcoin import Bitcoin


class Mineralscoin(Bitcoin):
    """
    Class with all the necessary Mineralscoin network information based on
    https://github.com/Minerals-dev/Minerals/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'mineralscoin'
    symbols = ('MIN', )
    seeds = ("dnsseed1.minerals.pro",
             "dnsseed2.minerals.pro")
    port = 33442
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 178
    }

# no testnet
