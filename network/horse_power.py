from clove.network.bitcoin import Bitcoin


class Horse_Power(Bitcoin):
    """
    Class with all the necessary Horse Power network information based on
    https://github.com/HorsePowerCoin/HorsePowerCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'horse_power'
    symbols = ('HSP', )
    seeds = ("45.55.236.105")
    port = 32421
	
# no testnet