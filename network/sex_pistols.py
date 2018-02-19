from clove.network.bitcoin import Bitcoin


class Sex_Pistols(Bitcoin):
    """
    Class with all the necessary Sex Pistols network information based on
    https://github.com/sexpist/sexpistols/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sex_pistols'
    symbols = ('SP', )
    seeds = ("node.walletbuilders.com")
    port = 7515
	
#  no testnet