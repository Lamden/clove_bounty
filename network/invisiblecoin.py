from clove.network.bitcoin import Bitcoin


class InvisibleCoin(Bitcoin):
    """
    Class with all the necessary InvisibleCoin network information based on
    https://github.com/ivzdev/invisiblecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'invisiblecoin'
    symbols = ('IVZ', )
    seeds = ("node1.invisiblecoin.net", "node2.invisiblecoin.net", )
    port = 28881
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 230
    }


# Has no testnet
