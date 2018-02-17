from clove.network.bitcoin import Bitcoin


class  Atmos(Bitcoin):
    """
    Class with all the necessary  Atmos (ATMS) network information based on
    https://github.com/asphyxiating/atmostemp/blob/master/atmos-master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'atmos'
    symbols = ('ATMS', )
    seeds =  ('212.129.37.112')
    port = 9834


class  AtmosTestNet(Atmos):
    """
    Class with all the necessary  Atmos (ATMS) network information based on
    https://github.com/asphyxiating/atmostemp/blob/master/atmos-master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-atmos'
    symbols = ('ATMS', )
    seeds =  ()
    port = 9835
