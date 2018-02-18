from clove.network.bitcoin import Bitcoin


class  Wagerr(Bitcoin):
    """
    Class with all the necessary  Wagerr (WGR) network information based on
    https://github.com/wagerr/wagerr/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'wagerr'
    symbols = ('WGR', )
    seeds =  ('main.seederv1.wgr.host', 'main.seederv2.wgr.host', 'main.devseeder1.wgr.host', 'main.devseeder2.wgr.host')
    port = 55002


class  WagerrTestNet(Wagerr):
    """
    Class with all the necessary  Wagerr (WGR) network information based on
    https://github.com/wagerr/wagerr/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-wagerr'
    symbols = ('WGR', )
    seeds =  ('test.testseederv1.wgr.host', 'test.testseederv2.wgr.host', 'test.devseeder1.wgr.host', 'test.devseeder2.wgr.host')
    port = 55004