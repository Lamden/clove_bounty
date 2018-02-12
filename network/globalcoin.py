from clove.network.bitcoin import Bitcoin


class GlobalCoin(Bitcoin):
    """
    Class with all the necessary CryptoBullion network information based on
    https://github.com/cryptogenicbonds/cryptobullion-cbx/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'globalcoin'
    symbols = ('GLC', )
    seeds =  ("ip 54.252.196.5", "ip 52.24.129.149")
    port = 55789
	
	
# Has no Testnet