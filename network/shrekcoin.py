from clove.network.bitcoin import Bitcoin


class ShrekCoin(Bitcoin):
    """
    Class with all the necessary ShrekCoin network information based on
    https://github.com/shrekcoin/shrek/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'shrekcoin'
    symbols = ('SHREK', )
    seeds = ("node.walletbuilders.com")
    port = 7443
    message_start = b'\x96\xc7\xb2\x6f'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

# no testnet
