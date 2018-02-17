from clove.network.bitcoin import Bitcoin


class JobsCoin(Bitcoin):
    """
    Class with all the necessary JobsCoin network information based on
    https://github.com/jobscoindev/jobscoin-source/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'jobscoin'
    symbols = ('JOBS', )
    seeds = ("seed1.jobscoin.us",
             "seed2.jobscoin.us",
             "seed3.jobscoin.us",
             "seed4.jobscoin.us")
    port = 9999
	
# No testnet
