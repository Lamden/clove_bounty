from clove.network.bitcoin import Bitcoin


class Chesscoin(Bitcoin):
    """
    Class with all the necessary chesscoin network information based on
    https://github.com/coinforchess/chesscoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Chesscoin'
    symbols = ('CHESS', )
    seeds =  ("node.walletbuilders.com")
    port = 7323


class ChesscoinTestNet(Chesscoin):
    """
    Class with all the necessary chesscoin testing network information based on
    https://github.com/coinforchess/chesscoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-Chesscoin'
    seeds = ()
    port = 17323        
	
	
	