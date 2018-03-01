
from clove.network.bitcoin import Bitcoin


class GameUnits(Bitcoin):
    """
    Class with all the necessary UNITS network information based on
    http://www.github.com/gameunits/gameunits/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'gameunits'
    symbols = ('UNITS', )
    seeds = ('151.80.95.45', '91.121.108.101', '5.196.89.126')
    port = 1338
    message_start = b'\x13\xfa\x37\x2f'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 115,
        'SECRET_KEY': 197
    }


class GameUnitsTestNet(GameUnits):
    """
    Class with all the necessary UNITS testing network information based on
    http://www.github.com/gameunits/gameunits/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-gameunits'
    seeds = ()
    port = 17997
    message_start = b'\xfa\x10\x70\x2f'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 177,
        'SECRET_KEY': 250
    }
