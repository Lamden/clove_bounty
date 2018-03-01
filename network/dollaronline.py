from clove.network.bitcoin import Bitcoin


class DollarOnline(Bitcoin):
    """
    Class with all the necessary DollarOnline network information based on
    https://github.com/dollar-online/dollar/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'dollaronline'
    symbols = ('DOLLAR', )
    seeds = ("91.109.38.231",
             "s01.edollar.online",
             "s02.edollar.online",
             "s03.edollar.online",
             "s04.edollar.online",
             "s05.edollar.online",
             "s06.edollar.online",
             "s07.edollar.online",
             "s08.edollar.online",
             "s09.edollar.online",
             "s10.edollar.online")
    port = 22888
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 90,
        'SECRET_KEY': 158
    }


# No Testnet
