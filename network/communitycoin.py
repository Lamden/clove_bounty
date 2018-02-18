from clove.network.bitcoin import Bitcoin


class CommunityCoin(Bitcoin):
    """
    Class with all the necessary CommunityCoin.py network information based on
    https://github.com/coolindark/communitycoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'communitycoin'
    symbols = ('COMM', )
    seeds = ("cocnode1.coolindark.com",
             "cocnode2.coolindark.com")	 
    port = 7643
	
# no testnet	