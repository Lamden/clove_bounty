from clove.network.bitcoin import Bitcoin


class Comet(Bitcoin):
    """
    Class with all the necessary Comet network information based on
    https://github.com/cmtcoin/wallet/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'comet'
    symbols = ('CMT', )
    seeds =  ("node.cometcoin.com")
    port = 7045
	
# Has no testnet