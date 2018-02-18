from clove.network.bitcoin import Bitcoin


class ConcealCoin(Bitcoin):
    """
    Class with all the necessary ConcealCoin network information based on
    https://github.com/concealcoin/concealcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'concealcoin'
    symbols = ('CNL', )
    seeds =  ("54.76.49.245")
    port = 27712
	
# Has no testnet