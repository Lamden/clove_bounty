from clove.network.bitcoin import Bitcoin


class Condensate(Bitcoin):
    """
    Class with all the necessary Condensate network information based on
    https://github.com/bumbacoin/rain-master/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'condensate'
    symbols = ('RAIN', )
    seeds = ("seed1.rain.trade",
             "seed2.rain.trade",
             "seed3.rain.trade",
             "seed4.rain.trade")
    port = 23373
	
