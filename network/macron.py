from clove.network.bitcoin import Bitcoin


class MACRON(Bitcoin):
    """
    Class with all the necessary MACRON network information based on
    https://github.com/macroncoin/macron/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'macron'
    symbols = ('MCRN', )
    nodes = ('192.52.167.209', )
    port = 55553
    message_start = b'\xa4\xd2\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 12,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 140
    }


# Has no testnet
