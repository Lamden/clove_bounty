from clove.network.bitcoin import Bitcoin


class F16Coin(Bitcoin):
    """
    Class with all the necessary F16Coin network information based on
    https://github.com/f16coin/air/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'f16coin'
    symbols = ('F16', )
    seeds = ("node.walletbuilders.com", )
    port = 18077
    message_start = b'\xac\x1e\xab\x45'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 163
    }

# no testnet
