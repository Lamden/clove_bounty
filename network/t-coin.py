from clove.network.bitcoin import Bitcoin


class T-coin(Bitcoin):
    """
    Class with all the necessary T-coin network information based on
    https://github.com/tcoindev/t-coin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 't-coin'
    symbols = ('TCOIN', )
    seeds = ("175.124.227.229",
             "175.124.227.230")
    port = 25286
