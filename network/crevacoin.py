from clove.network.bitcoin import Bitcoin


class CrevaCoin(Bitcoin):
    """
    Class with all the necessary CrevaCoin network information based on
    https://github.com/crevacoin/creva/blob/master/crevacoin_source/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'crevacoin'
    symbols = ('CREVA', )
    seeds =  ("123.57.60.128")
    port = 22440
	
   
class CrevaCoinTestNet(CrevaCoin):
    """
    Class with all the necessary CrevaCoin testing network information based on
    https://github.com/crevacoin/creva/blob/master/crevacoin_source/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-crevacoin'
    seeds = ("23.23.186.131")
    port = 22441              