from clove.network.bitcoin import Bitcoin


class PrismChain(Bitcoin):
    """
    Class with all the necessary PrismChain network information based on
    https://github.com/PrismChain/prm/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'prismchain'
    symbols = ('PRM', )
    seeds = ("146.185.169.104")
    port = 21995
    message_start = b'\xa2\xdc\xb1\xf7'
    base58_prefixes = {
        'PUBKEY_ADDR': 56,
        'SCRIPT_ADDR': 81,
        'SECRET_KEY': 184
    }

# no testnet
