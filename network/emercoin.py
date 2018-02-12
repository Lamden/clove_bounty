from clove.network.bitcoin import Bitcoin


class Emercoin(Bitcoin):
    """
    Class with all the necessary Emercoin EMC network information based on
    https://github.com/emercoin/emercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'emercoin'
    symbols = ('EMC', )
    seeds = ('seed.emercoin.com', 'seed.emercoin.net', 'seed.emergate.net', 'seed.emc')
    port = 6661


class EmercoinTestNet(Emercoin):
    """
    Class with all the necessary Emercoin EMC testing network information based on
    https://github.com/emercoin/emercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-emercoin'
    seeds = ('tnseed.emercoin.com')
    port = 6663
