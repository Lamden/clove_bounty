from clove.network.bitcoin import Bitcoin


class Particl(Bitcoin):
    """
    Class with all the necessary Particl PART network information based on
    https://github.com/particl/particl-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'particl'
    symbols = ('PART', )
    seeds = ('mainnet-seed.particl.io', 'dnsseed-mainnet.particl.io', 'mainnet.particl.io')
    port = 51738


class ParticlTestNet(Particl):
    """
    Class with all the necessary Particl PART testing network information based on
    https://github.com/particl/particl-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-particl'
    seeds = ('testnet-seed.particl.io', 'dnsseed-testnet.particl.io')
    port = 51938
