from clove.network.bitcoin import Bitcoin


class Unitus(Bitcoin):
    """
    Class with all the necessary UIS network information based on
    https://github.com/unitusdev/unitus/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'unitus'
    symbols = ('UIS', )
    seeds = (
        'core.easymine.online',
        'use.easymine.online',
        'us.nutty.one',
        'nz.nutty.one',
    )
    port = 50603


class UnitusTestNet(Unitus):
    """
    Class with all the necessary UIS testing network information based on
    https://github.com/unitusdev/unitus/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-unitus'
    seeds = (
        'testseed1.unitus.online',
        'testseed2.unitus.online',
    )
    port = 60603
