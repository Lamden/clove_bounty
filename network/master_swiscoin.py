from clove.network.bitcoin import Bitcoin


class Master_Swiscoin(Bitcoin):
    """
    Class with all the necessary Master Swiscoin network information based on
    https://github.com/SCNPay/Swiscoin-Master/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'master_swiscoin'
    symbols = ('MSCN', )
    seeds = ("188.166.182.57",
             "swisexplorer.com",
             "dns.swisexplorer.com")
    port = 20774
	
# no testnet
	
