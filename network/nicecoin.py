from clove.network.bitcoin import Bitcoin


class NiceCoin(Bitcoin):
    """
    Class with all the necessary NiceCoin network information based on
    https://github.com/nicecoinx/nicecoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'nicecoin'
    symbols = ('NICE', )
    seeds = ("5.101.119.57")
    port = 27730
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 181
    }

# no testnet
