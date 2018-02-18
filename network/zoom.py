from clove.network.bitcoin import Bitcoin


class Zoom(Bitcoin):
    """
    Class with all the necessary Zoom network information based on
    https://github.com/zoom-c/zoom/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'zoom'
    symbols = ('ZOOM', )
    seeds = ("seed.ZoomCoin.co",
             "45.32.199.52")
    port = 26889
	
   
