from clove.network.bitcoin import Bitcoin


class HomeBlockCoin(Bitcoin):
    """
    Class with all the necessary HomeBlockCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'homeblockcoin'
    symbols = ('HBC', )
    seeds = ("91.92.136.176",
             "91.92.128.161",
             "82.221.141.12")
    port = 45690
	
