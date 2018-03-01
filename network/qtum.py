from clove.network.bitcoin import Bitcoin


class Qtum(Bitcoin):
    """
    Class with all the necessary QTUM network information based on
    https://github.com/qtumproject/qtum/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'qtum'
    symbols = ('QTUM', )
    seeds = (
        'qtum3.dynu.net',
    )
    port = 3888
    message_start = b'\xf1\xcf\xa6\xd3'
    base58_prefixes = {
        'PUBKEY_ADDR': 58,
        'SCRIPT_ADDR': 50,
        'SECRET_KEY': 128
    }


class QtumTestNet(Qtum):
    """
    Class with all the necessary QTUM testing network information based on
    https://github.com/qtumproject/qtum/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-qtum'
    seeds = (
        'qtum4.dynu.net',
    )
    port = 13888
    message_start = b'\x0d\x22\x15\x06'
    base58_prefixes = {
        'PUBKEY_ADDR': 120,
        'SCRIPT_ADDR': 110,
        'SECRET_KEY': 239
    }
