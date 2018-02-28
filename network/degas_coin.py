from clove.network.bitcoin import Bitcoin


class Degas_Coin(Bitcoin):
    """
    Class with all the necessary Degas Coin network information based on
    https://github.com/Deacoin/dea-coin-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'degas_coin'
    symbols = ('DEA', )
    seeds = ("node.45.32.222.247")
    port = 12699

# no test net
