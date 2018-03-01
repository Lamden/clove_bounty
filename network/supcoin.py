from clove.network.bitcoin import Bitcoin


class Supcoin(Bitcoin):
    """
    Class with all the necessary Supcoin network information based on
    https://github.com/supcoin/supcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'supcoin'
    symbols = ('SUP', )
    seeds = ("sup1.earlz.net",
             "sup2.earlz.net",
             "sup3.earlz.net",
             "sup1.supcoin.com",
             "sup2.supcoin.com")
    port = 4411


class SupcoinTestNet(Supcoin):
    """
    Class with all the necessary Supcoin testing network information based on
    https://github.com/supcoin/supcoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-diamond'
    seeds = ("testnetsup.earlz.net")
    port = 14411
