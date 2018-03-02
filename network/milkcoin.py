from clove.network.bitcoin import Bitcoin


class MilkCoin(Bitcoin):
    """
    Class with all the necessary MilkCoin network information based on
    https://github.com/milkcoin/milk/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'milkcoin'
    symbols = ('MUU', )
    nodes = ("185.69.55.50", )
    port = 35235
    message_start = b'\xf1\xd5\xd1\xf2'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 55,
        'SECRET_KEY': 178
    }

# no testnet
