from clove.network.bitcoin import Bitcoin


class Cinder(Bitcoin):
    """
    Class with all the necessary Cinder network information based on
    https://github.com/CrypTraider/Cinder/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cinder'
    symbols = ('CIN', )
    seeds = ("104.156.253.23",
             "108.61.223.155",
             "104.236.49.247",
             "128.199.57.33")
    port = 22555

# Has no testnet
