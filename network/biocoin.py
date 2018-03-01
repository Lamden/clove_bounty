from clove.network.bitcoin import Bitcoin


class Biocoin(Bitcoin):
    """
    Class with all the necessary Biocoin network information based on
    https://github.com/Blackithart/biocoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'biocoin'
    symbols = ('BIO', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "seed4.cryptolife.net",
             "seed5.cryptolife.net")
    port = 24885
    message_start = b'\xb4\xf9\xe1\xa5'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 153
    }

# Has no testnet
