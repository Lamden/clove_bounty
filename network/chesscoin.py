from clove.network.bitcoin import Bitcoin


class Chesscoin(Bitcoin):
    """
    Class with all the necessary chesscoin network information based on
    https://github.com/coinforchess/chesscoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Chesscoin'
    symbols = ('CHESS', )
    seeds = ("node.walletbuilders.com", )
    port = 7323
    message_start = b'\xde\x3a\xae\x3c'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }


# Has no Testnet
