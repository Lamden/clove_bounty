
from clove.network.bitcoin import Bitcoin


class RideMyCar(Bitcoin):
    """
    Class with all the necessary RIDE network information based on
    http://www.github.com/RideMyCar/RideMyCar-Coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'ride-my-car'
    symbols = ('RIDE', )
    seeds = ('146.185.146.172',)
    port = 11517


class RideMyCarTestNet(RideMyCar):
    """
    Class with all the necessary RIDE testing network information based on
    http://www.github.com/RideMyCar/RideMyCar-Coin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-ride-my-car'
    seeds = ()
    port = 25713
