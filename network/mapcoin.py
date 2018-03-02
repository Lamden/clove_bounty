from clove.network.bitcoin import Bitcoin


class MapCoin(Bitcoin):
    """
    Class with all the necessary MapCoin network information based on
    https://github.com/mapcoindev/MAPCOIN/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mapcoin'
    symbols = ('MAPC', )
    nodes = ("104.236.105.49",
             "178.62.126.32",
             "95.85.39.251")
    port = 25214
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 178
    }
