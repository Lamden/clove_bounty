from clove.network.bitcoin import Bitcoin


class EmporiumCoin(Bitcoin):
    """
    Class with all the necessary EmporiumCoin network information based on
    https://github.com/emporiumcoin/EmporiumCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'emporiumcoin'
    symbols = ('EMPC', )
    seeds = ("40.68.31.20")
    port = 8295
    message_start = b'\xc2\xb4\xa3\xd1'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 161
    }

# no testnet
