from clove.network.bitcoin import Bitcoin


class WiserCoin(Bitcoin):
    """
    Class with all the necessary WiserCoin network information based on
    https://github.com/databir/WiserCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'wisercoin'
    symbols = ('WSC', )
    seeds = ("sec1.wisercoin.com",
             "sec2.wisercoin.com")
    port = 21777
	
