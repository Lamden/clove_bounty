from clove.network.bitcoin import Bitcoin


class Neurocoin(Bitcoin):
    """
    Class with all the necessary Neurocoin network information based on
    https://github.com/neurocoin/neurocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'neurocoin'
    symbols = ('NRO', )
    seeds = ("46.101.192.195",
             "188.226.150.84",
             "147.135.191.162")
    port = 17771
	
