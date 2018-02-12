from clove.network.bitcoin import Bitcoin


class Kurrent(Bitcoin):
    """
    Class with all the necessary Kurrent network information based on
    https://github.com/kurrentproject/kurrent/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'kurrent'
    symbols = ('KURT', )
    seeds = ('212.24.107.99')
    port = 18080


# Has no testnet