from clove.network.bitcoin import Bitcoin


class ArtexCoin(Bitcoin):
    """
    Class with all the necessary ArtexCoin network information based on
    https://github.com/johnhunt123/artexcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'artexcoin'
    symbols = ('ATX', )
    seeds = ("162.243.85.154",
             "162.243.99.178",
             "seed3.cryptolife.net",
             "electrum3.cryptolife.net")
    port = 14584
    message_start = b'\xfa\xc3\xbf\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 151
    }
