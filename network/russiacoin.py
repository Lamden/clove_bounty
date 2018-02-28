from clove.network.bitcoin import Bitcoin


class RussiaCoin(Bitcoin):
    """
    Class with all the necessary RussiaCoin network information based on
    https://github.com/russiacoindotinfo/russiacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'russiacoin'
    symbols = ('RC', )
    seeds = ("194.135.89.60")
    port = 19992


# Has no testnet
