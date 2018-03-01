from clove.network.bitcoin import Bitcoin


class ToaCoin(Bitcoin):
    """
    Class with all the necessary ToaCoin network information based on
    https://github.com/toacoin/TOA/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'toacoin'
    symbols = ('TOA', )
    seeds = ("212.24.111.232",
             "212.24.111.8",
             "212.24.111.34")
    port = 9642

# no test net
