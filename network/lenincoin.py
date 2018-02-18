from clove.network.bitcoin import Bitcoin


class LeninCoin(Bitcoin):
    """
    Class with all the necessary LeninCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'lenincoin'
    symbols = ('LENIN', )
    seeds = ("kicks.servep2p.com")
    port = 10157
	
# no testnet