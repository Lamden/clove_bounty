from clove.network.bitcoin import Bitcoin


class  Solarflarecoin(Bitcoin):
    """
    Class with all the necessary  Solarflarecoin (SFC) network information based on
    https://github.com/solarflareproject/solarflarecoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'solarflarecoin'
    symbols = ('SFC', )
    seeds =  ('54.152.17.29')
    port = 12387


class  SolarflarecoinTestNet(Solarflarecoin):
    """
    Class with all the necessary  Solarflarecoin (SFC) network information based on
    https://github.com/solarflareproject/solarflarecoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-solarflarecoin'
    symbols = ('SFC', )
    seeds =  ()
    port = 22387