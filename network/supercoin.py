from clove.network.bitcoin import Bitcoin


class SuperCoin(Bitcoin):
    """
    Class with all the necessary SuperCoin network information based on
    https://github.com/CryptoUnited-Clients/SuperCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'supercoin'
    symbols = ('SUPER', )
    seeds =  ("app1.super-coin.net", "app2.super-coin.net")
    port = 19390
	
   
class SuperCoinTestNet(SuperCoin):
    """
    Class with all the necessary SuperCoin testing network information based on
    https://github.com/CryptoUnited-Clients/SuperCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-supercoin'
    seeds = ()
    port = 29390              
	
	
	