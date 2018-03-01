from clove.network.bitcoin import Bitcoin


class EcoCoin(Bitcoin):
    """
    Class with all the necessary ECO network information based on
    https://github.com/ekocoin/eko/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'ecocoin'
    symbols = ('ECO', )
    seeds = ("node.walletbuilders.com")
    port = 7257
    message_start = b'\x8d\xb9\x92\x39'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 161
    }

# no testnet
