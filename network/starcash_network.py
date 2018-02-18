from clove.network.bitcoin import Bitcoin


class StarCashNetwork(Bitcoin):
    """
    Class with all the necessary StarCash Network (STARS) network information based on
    https://github.com/cybernetik7/StarCash-Network-2.0/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'starcashnetwork'
    symbols = ('STARS', )
    seeds = ('45.32.226.114')
    port = 21698

# no testnet
