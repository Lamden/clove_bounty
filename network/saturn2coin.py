from clove.network.bitcoin import Bitcoin


class Saturn2Coin(Bitcoin):
    """
    Class with all the necessary Saturn2Coin network information based on
    https://github.com/Flapmin/SAT2/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'saturn2coin'
    symbols = ('SAT2', )
    seeds = ("seed.saturn2coin.mycryptocoins.net",
             "seednodes.saturn2coin.mycryptocoins.net")
    port = 17771
    message_start = b'\xd3\xf4\xc3\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 191
    }

# no testnet
