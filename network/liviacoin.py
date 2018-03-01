from clove.network.bitcoin import Bitcoin


class LiviaCoin(Bitcoin):
    """
    Class with all the necessary LiviaCoin network information based on
    https://github.com/liviacoin/liv/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'liviacoin'
    symbols = ('LIV', )
    seeds = ("162.243.239.239")
    port = 42623

# no testnet
