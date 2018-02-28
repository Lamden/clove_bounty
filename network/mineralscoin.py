from clove.network.bitcoin import Bitcoin


class Mineralscoin(Bitcoin):
    """
    Class with all the necessary Mineralscoin network information based on
    https://github.com/Minerals-dev/Minerals/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'mineralscoin'
    symbols = ('MIN', )
    seeds = ("dnsseed1.minerals.pro",
             "dnsseed2.minerals.pro")
    port = 33442

# no testnet
