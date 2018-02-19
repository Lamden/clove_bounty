from clove.network.bitcoin import Bitcoin


class TenneT(Bitcoin):
    """
    Class with all the necessary TenneT network information based on
    https://github.com/TenneTCo/TenneT/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'tennet'
    symbols = ('TENNET', )
    seeds = ("52.26.15.236")
    port = 9782
	
# no testnet