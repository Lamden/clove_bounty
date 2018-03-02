from clove.network.bitcoin import Bitcoin


class Quicksilver(Bitcoin):
    """
    Class with all the necessary Quicksilver network information based on
    https://github.com/Quicksilvercoin/quicksilver/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'quicksilver'
    symbols = ('QSLV', )
    nodes = ("104.207.149.190",
             "45.32.246.198",
             "45.63.12.231")
    port = 21333
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 186
    }
