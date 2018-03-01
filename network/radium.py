
from clove.network.bitcoin import Bitcoin


class Radium(Bitcoin):
    """
    Class with all the necessary RADS network information based on
    http://www.github.com/RadiumCore/radium-0.11/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'radium'
    symbols = ('RADS', )
    seeds = ('52.23.134.122',)
    port = 27913
    message_start = b'\x2a\x7c\xcb\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 76,
        'SCRIPT_ADDR': 58,
        'SECRET_KEY': 121
    }


class RadiumTestNet(Radium):
    """
    Class with all the necessary RADS testing network information based on
    http://www.github.com/RadiumCore/radium-0.11/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-radium'
    seeds = ('35.153.123.156', '34.207.38.233')
    port = 47963
    message_start = b'\xc3\x77\xcc\x77'
    base58_prefixes = {
        'PUBKEY_ADDR': 110,
        'SCRIPT_ADDR': 129,
        'SECRET_KEY': 239
    }
