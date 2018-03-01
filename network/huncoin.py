from clove.network.bitcoin import Bitcoin


class Huncoin(Bitcoin):
    """
    Class with all the necessary Huncoin network information based on
    https://github.com/huncoin/huncoin/blob/huncoin/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'huncoin'
    symbols = ('HNC', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "electrum1.cryptolife.net")
    port = 22093
    message_start = b'\xaa\xcc\xb9\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 41,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 169
    }

# no testnet
