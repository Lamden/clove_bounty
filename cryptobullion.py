from clove.network.bitcoin import Bitcoin


class CryptoBullion(Bitcoin):
    """
    Class with all the necessary CryptoBullion network information based on
    https://github.com/cryptogenicbonds/cryptobullion-cbx/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cryptobullion'
    symbols = ('CBX', )
    seeds =  ("seed.cryptobullion.io")
    port = 7695
	
	
class CryptoBullionTestNet(CryptoBullion):
    """
    Class with all the necessary CryptoBullion testing network information based on
    https://github.com/cryptogenicbonds/cryptobullion-cbx/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-cryptobullion'
    seeds = ()
    port = 17695           
	
	
	