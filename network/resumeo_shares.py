from clove.network.bitcoin import Bitcoin


class Resumeo_Shares(Bitcoin):
    """
    Class with all the necessary Resumeo Shares network information based on
    https://github.com/vanyabios/resumeo/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'resumeo_shares'
    symbols = ('RMS', )
    seeds = ("107.170.189.185",
             "79.135.200.66")
    port = 38891
