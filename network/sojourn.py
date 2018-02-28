from clove.network.bitcoin import Bitcoin


class Sojourn(Bitcoin):
    """
    Class with all the necessary Sojourn network information based on
    https://github.com/sojournagain/Sojourn1.01/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'sojourn'
    symbols = ('SOJ', )
    seeds = ("35.165.166.142")
    port = 19951

# no testnet
