from clove.network.bitcoin import Bitcoin


class Cyder(Bitcoin):
    """
    Class with all the necessary Cyder (CYDER) network information based on
    https://github.com/cyderenergy/cyder/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'cyder'
    symbols = ('CYDER', )
    seeds = ('34.212.55.142')
    port = 48848

# no testnet
