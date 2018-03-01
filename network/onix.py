from clove.network.bitcoin import Bitcoin


class Onix(Bitcoin):
    """
    Class with all the necessary Onix network information based on
    https://github.com/onix-project/onixcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'onix'
    symbols = ('ONX', )
    seeds = ("seed5.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum6.cryptolife.net")
    port = 41016
    message_start = b'\xf3\xc3\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 203
    }
