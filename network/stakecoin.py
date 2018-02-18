from clove.network.bitcoin import Bitcoin


class Stakecoin(Bitcoin):
    """
    Class with all the necessary Stakecoin network information based on
    https://github.com/Cinnicoin/stakecoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'stakecoin'
    symbols = ('STCN', )
    seeds = ("nodea.stakecoin.co",
             "nodeb.stakecoin.co",
             "nodec.stakecoin.co")	
    port = 16814
	
# no testnet