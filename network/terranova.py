from clove.network.bitcoin import Bitcoin


class TerraNova(Bitcoin):
    """
    Class with all the necessary TerraNova network information based on
    https://github.com/TERRAcoin-source/TerraNova-src/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'terranova'
    symbols = ('TER', )
    seeds = ("194.87.96.140")
    port = 14542

# no testnet
