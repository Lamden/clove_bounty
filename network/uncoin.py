from clove.network.bitcoin import Bitcoin


class UNCoin(Bitcoin):
    """
    Class with all the necessary UNCoin network information based on
    https://github.com/belledejour/uncoin-source-code/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'UNCoin'
    symbols = ('UNC', )
    nodes = ('120.27.44.15', '114.215.178.237', '115.29.224.192', )
    port = 33156
    message_start = b'\x74\xf5\x1c\x61'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 196
    }


# Has no Testnet
