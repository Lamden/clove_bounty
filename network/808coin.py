from clove.network.bitcoin import Bitcoin


class Coin808(Bitcoin):
    """
    Class with all the necessary 808coin network information based on
    https://github.com/maxxine/808/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = '808coin'
    symbols = ('808', )
    seeds = ('dns.808bass.space')
    port = 8087


# Has no testnet