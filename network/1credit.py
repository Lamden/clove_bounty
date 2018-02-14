from clove.network.bitcoin import Bitcoin


class OneCredit(Bitcoin):
    """
    Class with all the necessary 404 Coin network information based on
    https://github.com/1credit/1credit/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = '1CRedit'
    symbols = ('1CR', )
    seeds =  ("testnet-seed.1credittools.com",
              "testnet-seed.weminemnc.com",
              "dnstest.1creditcoin.org")
    port = 6666
	
   
# Has no testnet
