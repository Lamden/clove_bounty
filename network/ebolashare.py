from clove.network.bitcoin import Bitcoin


class EbolaShare(Bitcoin):
    """
    Class with all the necessary EbolaShare network information based on
    https://github.com/Ebolashare/ebolashare/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'ebolashare'
    symbols = ('EBS', )
    seeds =  ("37.25.41.54")
    port = 9333
	
# no testnet