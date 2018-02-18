from clove.network.bitcoin import Bitcoin


class Null07(Bitcoin):
    """
    Class with all the necessary 007Coin network information based on
    https://github.com/007coindev/007coin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = '007Coin '
    symbols = ('007', )
    seeds = ("46.101.7.165")
    port = 11007
	
# no testnet