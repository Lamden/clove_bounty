from clove.network.bitcoin import Bitcoin


class JaneCoin(Bitcoin):
    """
    Class with all the necessary JaneCoin network information based on
    https://github.com/cryptominers-online/janecoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'janecoin'
    symbols = ('JANE', )
    nodes = ('107.170.156.17', )
    port = 13413
    message_start = b'\xb7\xf7\xe7\xee'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 171
    }

# no testnet
