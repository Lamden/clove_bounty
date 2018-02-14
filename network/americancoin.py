from clove.network.bitcoin import Bitcoin


class AmericanCoin(Bitcoin):
    """
    Class with all the necessary AmericanCoin network information based on
    https://github.com/AMCcoin/AmericanCoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'americancoin'
    symbols = ('AMC', )
    seeds =  ("node1.amccoin.com",
              "node2.amccoin.com",
              "node3.amccoin.com")
    port = 9056
	
# Has no testnet