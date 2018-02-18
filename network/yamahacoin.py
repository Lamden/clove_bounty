from clove.network.bitcoin import Bitcoin


class YamahaCoin(Bitcoin):
    """
    Class with all the necessary YamahaCoin network information based on
    https://github.com/yamahacoin/ymc-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'yamahacoin'
    symbols = ('YMC', )
    seeds = ("node.walletbuilders.com")
    port = 8003

# no testnet