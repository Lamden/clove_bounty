from clove.network.bitcoin import Bitcoin


class SelenCoin(Bitcoin):
    """
    Class with all the necessary SelenCoin network information based on
    https://github.com/SelenCoin/selencoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'selencoin'
    symbols = ('SEL', )
    seeds = ("88.99.47.154")
    port = 55552
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 186
    }

# no testnet
