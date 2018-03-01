from clove.network.bitcoin import Bitcoin


class Comet(Bitcoin):
    """
    Class with all the necessary Comet network information based on
    https://github.com/cmtcoin/wallet/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'comet'
    symbols = ('CMT', )
    seeds = ("node.cometcoin.com")
    port = 7045
    message_start = b'\x79\xc0\x7c\x31'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }

# Has no testnet
