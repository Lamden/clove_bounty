from clove.network.bitcoin import Bitcoin


class Manet_Coin(Bitcoin):
    """
    Class with all the necessary Manet_Coin network information based on
    https://github.com/Manetcoin/mat-source/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'manet_coin'
    symbols = ('MAT', )
    seeds = ("node.45.76.117.168")
    port = 17795

# no testnet
