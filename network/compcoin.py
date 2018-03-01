from clove.network.bitcoin import Bitcoin


class Compcoin(Bitcoin):
    """
    Class with all the necessary Compcoin network information based on
    https://github.com/compcoinproof/CompCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'compcoin'
    symbols = ('CMP', )
    seeds = ("52.24.217.223")
    port = 2668

# Has no testnet
