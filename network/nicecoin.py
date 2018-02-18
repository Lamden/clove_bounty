from clove.network.bitcoin import Bitcoin


class NiceCoin(Bitcoin):
    """
    Class with all the necessary NiceCoin network information based on
    https://github.com/nicecoinx/nicecoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'nicecoin'
    symbols = ('NICE', )
    seeds = ("5.101.119.57")
    port = 27730
	
# no testnet