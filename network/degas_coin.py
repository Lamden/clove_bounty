from clove.network.bitcoin import Bitcoin


class Degas_Coin(Bitcoin):
    """
    Class with all the necessary Degas Coin network information based on
    https://github.com/Deacoin/dea-coin-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'degas_coin'
    symbols = ('DEA', )
    seeds = ("node.45.32.222.247")
    port = 12699
    message_start = b'\x6a\x9a\xf9\xbb'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 158
    }

# no test net
