from clove.network.bitcoin import Bitcoin


class TheVeganInitiative(Bitcoin):
    """
    Class with all the necessary TheVeganInitiative network information based on
    https://github.com/theveganinitiative/xve/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'theveganinitiative'
    symbols = ('XVE', )
    seeds = ("35.166.132.29")
    port = 53348


# has no testnet
