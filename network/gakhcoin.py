from clove.network.bitcoin import Bitcoin


class GAKHcoin(Bitcoin):
    """
    Class with all the necessary GAKHcoin network information based on
    https://github.com/gakh/GAKHcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'gakhcoin'
    symbols = ('GAKH', )
    seeds = ("46.166.168.155")
    port = 7829
	
# no testnet