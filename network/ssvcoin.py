from clove.network.bitcoin import Bitcoin


class SSVCoin(Bitcoin):
    """
    Class with all the necessary SSVCoin network information based on
    https://github.com/SSVDevTeam/SSVCoin/blob/master/SSVCoin/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ssvcoin'
    symbols = ('SSV', )
    seeds = ("91.246.70.114")
    port = 9235
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 191
    }

# no testnet
