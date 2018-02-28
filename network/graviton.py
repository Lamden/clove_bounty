from clove.network.bitcoin import Bitcoin


class Graviton(Bitcoin):
    """
    Class with all the necessary Graviton network information based on
    https://github.com/gravitondev/graviton/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'graviton'
    symbols = ('GRAV', )
    seeds = ("seed.graviton.ninja")
    port = 31321

# no testnet
