from clove.network.bitcoin import Bitcoin


class Marijuanacoin(Bitcoin):
    """
    Class with all the necessary Marijuanacoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'marijuanacoin'
    symbols = ('MAR', )
    seeds = ("marijuanacoin.org",
             "seed1.marijuanacoin.org",
             "seed2.marijuanacoin.org")
    port = 18829
	
