from clove.network.bitcoin import Bitcoin


class Concoin(Bitcoin):
    """
    Class with all the necessary Concoin network information based on
    https://github.com/Concoin/concoin-master/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'concoin'
    symbols = ('CONX', )
    seeds = ("94.176.236.84",
             "212.47.238.107",
             "94.176.235.111")
    port = 40100
