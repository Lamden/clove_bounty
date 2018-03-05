from clove.network.bitcoin import Bitcoin


class Zclassic(Bitcoin):
    """
    Class with all the necessary ZCL network information based on
    https://github.com/z-classic/zclassic/blob/master/src/chainparams.cpp
    (date of access: 01/18/2018)
    """
    name = 'zclassic'
    symbols = ('ZCL', )
    seeds = (
        'na1.zclassic.org',
        'na2.zclassic.org',
        'na3.zclassic.org',
        'eu1.zclassic.org',
        'eu2.zclassic.org',
        'eu3.zclassic.org',
        'as1.zclassic.org',
        'as2.zclassic.org',
        'as3.zclassic.org',
        'seed.zcl.chains.run',
        'dnsseed.indieonion.org',
        'dnsseed.rotorproject.org',
    )
    port = 8033


class ZclassicTestNet(Zclassic):
    """
    Class with all the necessary ZCL testing network information based on
    https://github.com/z-classic/zclassic/blob/master/src/chainparams.cpp
    (date of access: 01/18/2018)
    """
    name = 'test-zclassic'
    seeds = ('dnsseed.testnet.zclassic.org', )
    port = 18233
