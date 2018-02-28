from clove.network.bitcoin import Bitcoin


class Yenten(Bitcoin):
    """
    Class with all the necessary  Yenten (YTN) network information based on
    https://github.com/conan-equal-newone/yenten/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'yenten'
    symbols = ('YTN', )
    seeds = ('seed.yenten.org')
    port = 9981


class YentenTestNet(Yenten):
    """
    Class with all the necessary  Yenten (YTN) network information based on
    https://github.com/conan-equal-newone/yenten/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-yenten'
    symbols = ('YTN', )
    seeds = ()
    port = 19981
