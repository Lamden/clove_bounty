from clove.network.bitcoin import Bitcoin


class Hexx(Bitcoin):
    """
    Class with all the necessary Hexx network information based on
    https://github.com/hexxcointakeover/hexxcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Hexx'
    symbols = ('HXX', )
    seeds = ("76.74.170.249")
    port = 29100


# Has no Testnet

