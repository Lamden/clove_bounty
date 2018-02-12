from clove.network.bitcoin import Bitcoin


class IncaKoin(Bitcoin):
    """
    Class with all the necessary IncaKoin network information based on
    https://github.com/madross/incakoin-new/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'incakoin'
    symbols = ('NKA', )
    seeds = ('81.100.233.136')
    port = 17421


# Has no testnet