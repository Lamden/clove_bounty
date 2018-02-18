from clove.network.bitcoin import Bitcoin


class CludCoin(Bitcoin):
    """
    Class with all the necessary CludCoin network information based on
    https://github.com/allaboutbit/Cludcoin-project/blob/cludcoin/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cludcoin'
    symbols = ('CLUD', )
    seeds =  ("node.walletbuilders.com")
    port = 6959
	
# Has no testnet