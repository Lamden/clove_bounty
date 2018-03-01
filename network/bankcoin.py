from clove.network.bitcoin import Bitcoin


class Bankcoin(Bitcoin):
    """
    Class with all the necessary Bankcoin network information based on
    https://github.com/bankcoin18/bankcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'bankcoin'
    symbols = ('B@', )
    seeds = ("172.104.187.169", "172.104.173.190")
    port = 32886

# Has no testnet
