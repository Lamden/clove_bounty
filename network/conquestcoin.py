from clove.network.bitcoin import Bitcoin


class Conquestcoin(Bitcoin):
    """
    Class with all the necessary Conquestcoin network information based on
    https://github.com/jlong187/conquestcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'conquestcoin'
    symbols = ('CQST', )
    seeds =  ("216.31.12.30")
    port = 7837
	
# Has no testnet