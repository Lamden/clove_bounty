from clove.network.bitcoin import Bitcoin


class DeltaCredits(Bitcoin):
    """
    Class with all the necessary DeltaCredits network information based on
    https://github.com/Gladimor/DeltaCredits/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'deltacredits'
    symbols = ('DCRE', )
    seeds =  ("108.61.72.49")
    port = 31414
	
# Has no testnet