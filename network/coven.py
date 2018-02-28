from clove.network.bitcoin import Bitcoin


class Coven(Bitcoin):
    """
    Class with all the necessary Coven network information based on
    https://github.com/covencoin/coven2/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'coven'
    symbols = ('COV', )
    seeds = ("104.238.182.76")
    port = 83350

# Has no testnet
