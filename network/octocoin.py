from clove.network.bitcoin import Bitcoin


class  OctoCoin(Bitcoin):
    """
    Class with all the necessary  OctoCoin (888) network information based on
    https://github.com/octocoin-project/octocoin/blob/master-0.10/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'octocoin'
    symbols = ('888', )
    seeds =  ('octocoin.seeds.securepayment.cc')
    port = 22889


class  OctoCoinTestNet(OctoCoin):
    """
    Class with all the necessary  OctoCoin (888) network information based on
    https://github.com/octocoin-project/octocoin/blob/master-0.10/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-octocoin'
    symbols = ('888', )
    seeds =  ('octocoin.seeds.securepayment.cc')
    port = 32889