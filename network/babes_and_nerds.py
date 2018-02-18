from clove.network.bitcoin import Bitcoin


class Babes_and_Nerds(Bitcoin):
    """
    Class with all the necessary Babes and Nerds network information based on
    https://github.com/marksize/lowered/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'babes_and_nerds'
    symbols = ('ban', )
    seeds = ("52.88.144.119")
    port = 44258
	
# no testnet