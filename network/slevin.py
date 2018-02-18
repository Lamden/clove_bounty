from clove.network.bitcoin import Bitcoin


class Slevin(Bitcoin):
    """
    Class with all the necessary Slevin (SLEVIN) network information based on
    https://github.com/slevinseven/slevin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'slevin'
    symbols = ('SLEVIN', )
    seeds = ('35.160.130.225')
    port = 47748

# no testnet
