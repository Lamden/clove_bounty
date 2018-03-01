from clove.network.bitcoin import Bitcoin


class LimitedCoin(Bitcoin):
    """
    Class with all the necessary LimitedCoin network information based on
    https://github.com/LimitedCoin/LimitedCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'limitedcoin'
    symbols = ('LTD', )
    seeds = ("limitedcoin.dyndns.org")
    port = 39569

# no testnet
