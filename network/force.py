from clove.network.bitcoin import Bitcoin


class Force(Bitcoin):
    """
    Class with all the necessary Force (FOR) network information based on
    https://github.com/forceunited/force/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'force'
    symbols = ('FOR', )
    seeds = ('94.130.107.201', '45.77.201.147')
    port = 37246

# no testnet
