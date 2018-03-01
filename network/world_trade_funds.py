from clove.network.bitcoin import Bitcoin


class WorldTradeFunds(Bitcoin):
    """
    Class with all the necessary World Trade Funds network information based on
    https://github.com/wtfteam/wtfcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'world_trade_funds'
    symbols = ('XWT', )
    nodes = ("107.170.189.185",
             "144.76.139.212")
    port = 42733
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 98,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 226
    }
