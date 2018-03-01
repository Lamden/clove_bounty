from clove.network.bitcoin import Bitcoin


class GoldReserve(Bitcoin):
    """
    Class with all the necessary GoldReserve network information based on
    https://github.com/mesterlovesz74/goldreserve/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'goldreserve'
    symbols = ('XGR', )
    seeds = ('108.61.103.33', '5.250.177.24')
    port = 21192
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 166
    }
