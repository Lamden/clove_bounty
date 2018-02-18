from clove.network.bitcoin import Bitcoin


class TimesCoin(Bitcoin):
    """
    Class with all the necessary TimesCoin network information based on
    https://github.com/norens/timescoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'timescoin'
    symbols = ('TMC', )
    seeds = ("andarazoroflove.org")
    port = 55884
	
# no testnet