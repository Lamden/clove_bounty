from clove.network.bitcoin import Bitcoin


class Twelve(Bitcoin):
    """
    Class with all the necessary Twelve network information based on
    https://github.com/T-Inside/twelve/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'twelve'
    symbols = ('TWLV', )
    seeds = ("46.101.21.51",
             "46.101.155.214")
    port = 29662
	
