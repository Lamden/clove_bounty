from clove.network.bitcoin import Bitcoin


class CageCoin(Bitcoin):
    """
    Class with all the necessary CageCoin network information based on
    https://github.com/cagecoin/cagecoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'cagecoin'
    symbols = ('CAGE', )
    seeds = ("seed.cagecoin.com")
    port = 33112
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 31,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 159
    }

# no testnet
