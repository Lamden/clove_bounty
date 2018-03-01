from clove.network.bitcoin import Bitcoin


class Luxmi(Bitcoin):
    """
    Class with all the necessary Luxmi network information based on
    https://github.com/luxmicoin/Luxmi/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'luxmi'
    symbols = ('LXM', )
    seeds = ("luxmi.point2this.com", "46.101.75.37")
    port = 42192

# no testnet
