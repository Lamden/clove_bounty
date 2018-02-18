from clove.network.bitcoin import Bitcoin


class Evotion(Bitcoin):
    """
    Class with all the necessary Evotion (EVO) network information based on
    https://github.com/evoshiun/Evotion/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'evotion'
    symbols = ('EVO', )
    seeds = ('52.33.170.107')
    port = 9393

# no testnet
