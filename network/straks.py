from clove.network.bitcoin import Bitcoin


class STRAKS(Bitcoin):
    """
    Class with all the necessary STRAKS network information based on
    https://github.com/straks/straks/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'straks'
    symbols = ('STAK', )
    seeds = ("sm001.alphaqub.com",
             "sm002.alphaqub.com",
             "sm003.alphaqub.com",
             "sm004.alphaqub.com",
             "sm005.alphaqub.com")
    port = 7575
	
   
class STRAKSTestNet(STRAKS):
    """
    Class with all the necessary STRAKS testing network information based on
    https://github.com/straks/straks/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-straks'
    seeds = ("st001.radixpi.com",
             "st002.radixpi.com")
    port = 7565              
	
