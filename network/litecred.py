from clove.network.bitcoin import Bitcoin


class Litecred(Bitcoin):
    """
    Class with all the necessary Litecred network information based on
    https://github.com/Litecred-Project/Litecred/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'litecred'
    symbols = ('LTCR', )
    seeds = ("litenode1.litecred.org",
             "litenode2.litecred.org")
    port = 8868
	
   
