from clove.network.bitcoin import Bitcoin


class XG_Sports(Bitcoin):
    """
    Class with all the necessary xg_sports network information based on
    https://github.com/XGCoin/XG/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xg_sports'
    symbols = ('XG', )
    seeds = ("107.170.189.185")
    port = 52733
	
# no testnet