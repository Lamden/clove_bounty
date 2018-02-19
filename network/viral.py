from clove.network.bitcoin import Bitcoin


class Viral(Bitcoin):
    """
    Class with all the necessary Viral network information based on
    https://github.com/covertress/viral-qt/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'viral'
    symbols = ('VIRAL', )
    seeds = ("45.55.218.62")
    port = 28110
	
# no testnet