from clove.network.bitcoin import Bitcoin


class WarCoin(Bitcoin):
    """
    Class with all the necessary WarCoin network information based on
    https://github.com/warcoindev/WarCoin/blob/master/warcoin-source/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'warcoin'
    symbols = ('WRC', )
    seeds = ("node.walletbuilders.com")
    port = 10395
    message_start = b'\x2d\xa3\x00\xbc'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 201
    }

# no testnet
