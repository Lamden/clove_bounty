from clove.network.bitcoin import Bitcoin


class MIScoin(Bitcoin):
    """
    Class with all the necessary MIScoin network information based on
    https://github.com/miscoinproject/miscoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'miscoin'
    symbols = ('DMD', )
    seeds = ("seed1.miscoin.org",
             "seed2.miscoin.org") 
	port = 14552

# no testnet