from clove.network.bitcoin import Bitcoin


class Linda(Bitcoin):
    """
    Class with all the necessary LINDA network information based on
    https://github.com/lindacoin/linda/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'linda'
    symbols = ('LINDA', )
    seeds = ()
    port = 33820


class LindaTestNet(Linda):
    """
    Class with all the necessary LINDA testing network information based on
    https://github.com/lindacoin/linda/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-linda'
    seeds = ()
    port = 28888