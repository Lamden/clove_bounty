from clove.network.bitcoin import Bitcoin


class Ravencoin(Bitcoin):
    """
    Class with all the necessary RVN network information based on
    https://github.com/RavenProject/Ravencoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'raven'
    symbols = ('RVN', )
    seeds = (
        "seed-raven.ravencoin.org",
        "seed-raven.bitactivate.com"
    )
    port = 8767


class RavencoinTestNet(Ravencoin):
    """
    Class with all the necessary RVN testing network information based on
    https://github.com/RavenProject/Ravencoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-raven'
    seeds = (
        "seed-testnet-raven.ravencoin.org",
        "seed-testnet-raven.bitactivate.com"
    )
    port = 18767
