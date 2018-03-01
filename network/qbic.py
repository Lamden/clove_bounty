from clove.network.bitcoin import Bitcoin


class Qbic(Bitcoin):
    """
    Class with all the necessary Qbic (QBIC) network information based on
    https://github.com/qbic-platform/qbic/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'qbic'
    symbols = ('QBIC', )
    seeds = ('seed.qbic.io', )
    port = 17195


class QbicTestNet(Qbic):
    """
    Class with all the necessary Qbic (QBIC) testing network information based on
    https://github.com/qbic-platform/qbic/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-qbic'
    seeds = ('testnet-dns.qbic.io', )
    port = 18196
