
from clove.network.bitcoin import Bitcoin


class PureVidz(Bitcoin):
    """
    Class with all the necessary VIDZ network information based on
    http://www.github.com/purevidz/vidzcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'purevidz'
    symbols = ('VIDZ', )
    seeds = ('163.172.70.91',)
    port = 3818


class PureVidzTestNet(PureVidz):
    """
    Class with all the necessary VIDZ testing network information based on
    http://www.github.com/purevidz/vidzcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-purevidz                '
    seeds = ()
    port = 3918
