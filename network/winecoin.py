from clove.network.bitcoin import Bitcoin


class Winecoin(Bitcoin):
    """
    Class with all the necessary Winecoin network information based on
    https://github.com/winecoindev/winecoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'winecoin'
    symbols = ('WINE', )
    seeds = ("198.199.90.93")
    port = 18473

# no testnet
