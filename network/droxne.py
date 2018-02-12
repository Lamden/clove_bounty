from clove.network.bitcoin import Bitcoin


class DROXNE(Bitcoin):
    """
    Class with all the necessary DROXNE network information based on
    https://github.com/droxdev/drox/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'droxne'
    symbols = ('DRXNE', )
    seeds = ("198.199.90.93","45.55.89.248")
    port = 41241

	
# No Testnet