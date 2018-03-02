from clove.network.bitcoin import Bitcoin


class Compcoin(Bitcoin):
    """
    Class with all the necessary Compcoin network information based on
    https://github.com/compcoinproof/CompCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'compcoin'
    symbols = ('CMP', )
    nodes = ("52.24.217.223", )
    port = 2668
    message_start = b'\xb1\xb6\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 156
    }

# Has no testnet
