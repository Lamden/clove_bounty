from clove.network.bitcoin import Bitcoin


class Allsafe(Bitcoin):
    """
    Class with all the necessary Photon network information based on
    https://github.com/securitybank/allsafe2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'allsafe'
    symbols = ('ASAFE2', )
    seeds = ("63.142.254.223")
    port = 30234

# Has no testnet