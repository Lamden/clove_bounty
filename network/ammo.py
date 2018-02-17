from clove.network.bitcoin import Bitcoin


class  Ammo(Bitcoin):
    """
    Class with all the necessary  Ammo Reloaded (AMMO) network information based on
    https://github.com/AmmoCore/AmmoReloaded/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ammo'
    symbols = ('AMMO', )
    seeds =  ('ammoreloaded.io')
    port = 21582


class  AmmoTestNet(Aces):
    """
    Class with all the necessary  Ammo Reloaded (AMMO) network information based on
    https://github.com/AmmoCore/AmmoReloaded/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-ammo'
    symbols = ('AMMO', )
    seeds =  ()
    port = 28582