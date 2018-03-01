from clove.network.bitcoin import Bitcoin


class Sphere(Bitcoin):
    """
    Class with all the necessary Sphere (SPHR) network information based on
    https://github.com/SphereDevs/sphere/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'sphere'
    symbols = ('SPHR', )
    seeds = ('162.243.247.203', '162.243.25.133',
             '104.236.163.165', 'gqunlgogqx7x42zy.onion')
    port = 37544

# no testnet
