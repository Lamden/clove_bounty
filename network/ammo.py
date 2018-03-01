from clove.network.bitcoin import Bitcoin


class Ammo(Bitcoin):
    """
    Class with all the necessary  Ammo Reloaded (AMMO) network information based on
    https://github.com/AmmoCore/AmmoReloaded/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ammo'
    symbols = ('AMMO', )
    seeds = ('ammoreloaded.io', )
    port = 21582
    message_start = b'\xc3\xc5\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 14,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 142
    }


class AmmoTestNet(Ammo):
    """
    Class with all the necessary  Ammo Reloaded (AMMO) network information based on
    https://github.com/AmmoCore/AmmoReloaded/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-ammo'
    symbols = ('AMMO', )
    seeds = ()
    port = 28582
