from clove.network.bitcoin import Bitcoin


class PutinCoin(Bitcoin):
    """
    Class with all the necessary PutinCoin network information based on
    https://github.com/putincoinput/putincoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'putincoin'
    symbols = ('PUT', )
    seeds = ("45.76.1.121", "45.76.187.49")
    port = 20095
