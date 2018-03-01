from clove.network.bitcoin import Bitcoin


class CrankCoin(Bitcoin):
    """
    Class with all the necessary class CrankCoin network information based on
    https://github.com/joshafest/CrankCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'crankcoin'
    symbols = ('CRNK', )
    seeds = ("192.99.32.58")
    port = 17771
    message_start = b'\xaa\xa2\xb2\xc4'
    base58_prefixes = {
        'PUBKEY_ADDR': 11,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 139
    }

# Has no testnet
