from clove.network.bitcoin import Bitcoin


class ChanCoin(Bitcoin):
    """
    Class with all the necessary ChanCoin network information based on
    https://github.com/CHANCOIN/CHANCOIN/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'chancoin'
    symbols = ('CHAN', )
    seeds =  ("node.walletbuilders.com")
    port = 19117
	
# Has no testnet