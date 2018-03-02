from clove.network.bitcoin import Bitcoin


class NodeCoin(Bitcoin):
    """
    Class with all the necessary NodeCoin network information based on
    https://github.com/nodecoins/sources/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'nodecoin'
    symbols = ('NODC', )
    nodes = ('212.8.251.4', )
    port = 9219
    message_start = b'\x0c\x06\x7b\x67'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 181
    }


# Has no testnet
