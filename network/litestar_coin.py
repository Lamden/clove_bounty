from clove.network.bitcoin import Bitcoin


class Litestar_Coin(Bitcoin):
    """
    Class with all the necessary Litestar Coin network information based on
    https://github.com/rbsup2/ts3/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'litestar_coin'
    symbols = ('LTS', )
    seeds = ("52.10.106.228")
    port = 39230

# no testnet
