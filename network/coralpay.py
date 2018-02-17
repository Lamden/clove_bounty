from clove.network.bitcoin import Bitcoin


class CoralPay(Bitcoin):
    """
    Class with all the necessary CoralPay network information based on
    https://github.com/coralpay/coral/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'coralpay'
    symbols = ('CORAL', )
    seeds =  ("35.163.164.145")
    port = 60093
	
# Has no testnet