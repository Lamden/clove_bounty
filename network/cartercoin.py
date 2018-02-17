from clove.network.bitcoin import Bitcoin


class CarterCoin(Bitcoin):
    """
    Class with all the necessary CarterCoin network information based on
    https://github.com/cartercar/cartercoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cartercoin'
    symbols = ('CTC', )
    seeds =  ("andarazoroflove.org")
    port = 55884
	
# Has no testnet