from clove.network.bitcoin import Bitcoin


class Autumncoin(Bitcoin):
    """
    Class with all the necessary Autumncoin network information based on
    https://github.com/Autumncoindev/ATM/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'autumncoin'
    symbols = ('ATM', )
    seeds = ("192.241.204.48")
    port = 58851

# Has no testnet
