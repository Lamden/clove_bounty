from clove.network.bitcoin import Bitcoin


class SteneumCoin(Bitcoin):
    """
    Class with all the necessary SteneumCoin network information based on
    https://github.com/dhabitafx/steneum/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'steneumcoin'
    symbols = ('STN', )
    seeds =  ("64.20.57.229")
    port = 26965
	
   
# Has no Testnet