from clove.network.bitcoin import Bitcoin


class XGSports(Bitcoin):
    """
    Class with all the necessary xg_sports network information based on
    https://github.com/XGCoin/XG/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xg_sports'
    symbols = ('XG', )
    nodes = ("107.170.189.185", )
    port = 52733
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 98,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 226
    }

# no testnet
