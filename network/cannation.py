from clove.network.bitcoin import Bitcoin


class Cannation(Bitcoin):
    """
    Class with all the necessary Cannation network information based on
    https://github.com/cannationproject/cannation/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Cannation'
    symbols = ('CNNC', )
    seeds = ("195.74.52.227", "149.56.154.65")
    port = 12367


# Has no Testnet
