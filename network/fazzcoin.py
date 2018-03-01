from clove.network.bitcoin import Bitcoin


class Fazzcoin(Bitcoin):
    """
    Class with all the necessary Fazzcoin network information based on
    https://github.com/calzavara/Fazzcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'fazzcoin'
    symbols = ('FAZZ', )
    seeds = ("seed4.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum1.cryptolife.net",
             "wallet.cryptolife.net",
             "explore.cryptolife.net")
    port = 32263
    message_start = b'\xbb\xf8\xec\xf3'
    base58_prefixes = {
        'PUBKEY_ADDR': 31,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 159
    }
