from clove.network.bitcoin import Bitcoin


class Rupaya(Bitcoin):
    """
    Class with all the necessary Rupaya network information based on
    https://github.com/rupaya-project/rupaya/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'rupaya'
    symbols = ('RUPX', )
    seeds = ("dns.rupx.io",
             "209.250.241.176",
             "209.250.243.131",
             "45.77.239.108",
             "107.191.44.102",
             "144.202.0.206")
    port = 9020


class RupayaTestNet(Rupaya):
    """
    Class with all the necessary Rupaya testing network information based on
    https://github.com/rupaya-project/rupaya/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-rupaya'
    seeds = ("207.148.0.129",
             "45.77.239.30",
             "45.76.226.204")
    port = 51434
