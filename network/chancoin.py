from clove.network.bitcoin import Bitcoin


class ChanCoin(Bitcoin):
    """
    Class with all the necessary ChanCoin network information based on
    https://github.com/CHANCOIN/CHANCOIN/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'chancoin'
    symbols = ('CHAN', )
    seeds = ("node.walletbuilders.com")
    port = 19117
    message_start = b'\x0f\x91\x54\xf8'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }

# Has no testnet
