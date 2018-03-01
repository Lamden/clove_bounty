from clove.network.bitcoin import Bitcoin


class Elacoin(Bitcoin):
    """
    Class with all the necessary Elacoin network information based on
    https://github.com/thercg/elacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'elacoin'
    symbols = ('ELC', )
    seeds = ("51.255.6.35", "91.203.142.168")
    port = 9223
    message_start = b'\x37\x1c\xc4\xbf'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 161
    }


# Has no testnet
