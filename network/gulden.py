from clove.network.bitcoin import Bitcoin


class Gulden(Bitcoin):
    """
    Class with all the necessary Gulden network information based on
    https://github.com/Gulden/gulden-official/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'gulden'
    symbols = ('NLG', )
    seeds = ("seed.gulden.com",
             "rotterdam.gulden.network")
    port = 9231
	
   
class GuldenTestNet(Gulden):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/Gulden/gulden-official/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-gulden'
    seeds = ("testseed.gulden.blue",
             "testseed.gulden.network",
             "testseed.coinpool.nl")
    port = 9923              
	

	
