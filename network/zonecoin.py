from clove.network.bitcoin import Bitcoin


class Zonecoin(Bitcoin):
    """
    Class with all the necessary Zonecoin network information based on
    https://github.com/st4yinth3d4rk/zonecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'zonecoin'
    symbols = ('ZNE', )
    seeds = ("46.101.95.7", "146.185.147.21")
    port = 7901


# Has no testnet
