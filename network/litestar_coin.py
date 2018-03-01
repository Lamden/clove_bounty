from clove.network.bitcoin import Bitcoin


class LitestarCoin(Bitcoin):
    """
    Class with all the necessary Litestar Coin network information based on
    https://github.com/rbsup2/ts3/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'litestar_coin'
    symbols = ('LTS', )
    nodes = ("52.10.106.228", )
    port = 39230
    message_start = b'\xf0\xfb\xdb\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 201
    }

# no testnet
