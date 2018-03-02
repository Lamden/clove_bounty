from clove.network.bitcoin import Bitcoin


class CryptoCircuits(Bitcoin):
    """
    Class with all the necessary CryptoCircuits network information based on
    https://github.com/cryptocircuits/circuits/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptocircuits'
    symbols = ('CIRC', )
    nodes = ("188.166.126.155",
             "46.101.29.142")
    port = 28112
    message_start = b'\x28\x44\x15\x06'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 132,
        'SECRET_KEY': 171
    }

# Has no testnet
