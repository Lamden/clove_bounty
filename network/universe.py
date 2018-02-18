from clove.network.bitcoin import Bitcoin


class Universe(Bitcoin):
    """
    Class with all the necessary Universe (UNI) network information based on
    https://github.com/UniverseUNI/Universe-UNI/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'universe'
    symbols = ('UNI', )
    seeds = ('seed.unicoin.pw', 'seed2.unicoin.pw')
    port = 11029

# no testnet
