from clove.network.bitcoin import Bitcoin


class Madcoin(Bitcoin):
    """
    Class with all the necessary Madcoin network information based on
    https://github.com/madcoin-project/madcoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'madcoin'
    symbols = ('MDC', )
    seeds = ("block.madcoin.life",
             "node1.madcoin.life",
             "node2.madcoin.life")
    port = 10882
    message_start = b'\x35\x2c\x46\x51'
    base58_prefixes = {
        'PUBKEY_ADDR': 110,
        'SCRIPT_ADDR': 44,
        'SECRET_KEY': 142
    }

# no testnet
