from clove.network.bitcoin import Bitcoin


class Runners(Bitcoin):
    """
    Class with all the necessary Runners (RUNNERS) network information based on
    https://github.com/runnersdev/runners-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'runners'
    symbols = ('RUNNERS', )
    seeds = ('104.200.67.104')
    port = 20649

# no testnet
