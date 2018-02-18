from clove.network.bitcoin import Bitcoin


class BitCrystal(Bitcoin):
    """
    Class with all the necessary BitCrystal network information based on
    https://github.com/bitcrystal/bitcrystal_v20/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitcrystal'
    symbols = ('BTCRY', )
    seeds =  ("176.57.143.201")
    port = 9299
	
# Has no testnet