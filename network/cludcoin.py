from clove.network.bitcoin import Bitcoin


class CludCoin(Bitcoin):
    """
    Class with all the necessary CludCoin network information based on
    https://github.com/allaboutbit/Cludcoin-project/blob/cludcoin/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cludcoin'
    symbols = ('CLUD', )
    seeds = ("node.walletbuilders.com")
    port = 6959
    message_start = b'\xae\x20\x2d\xb0'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }

# Has no testnet
