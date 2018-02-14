from clove.network.bitcoin import Bitcoin


class CleverHash(Bitcoin):
    """
    Class with all the necessary CleverHash network information based on
    https://github.com/Cleverhash/CHASH/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cleverhash'
    symbols = ('CHASH', )
    seeds =  ("104.131.197.190","104.236.15.167")
    port = 28194
	
# Has no testnet