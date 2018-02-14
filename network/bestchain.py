from clove.network.bitcoin import Bitcoin


class BestChain(Bitcoin):
    """
    Class with all the necessary BestChain network information based on
    https://github.com/BestChain/Source/blob/BestChain/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bestchain '
    symbols = ('BEST', )
    seeds =  ("54.68.215.235",
              "95.211.57.108",
              "94.23.216.214",
              "81.169.212.185",
              "185.16.41.61")
    port = 47949
	
# Has no testnet