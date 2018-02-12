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
	
   
# Has no Testnet