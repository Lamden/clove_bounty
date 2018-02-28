from clove.network.bitcoin import Bitcoin


class BlackholeCoin(Bitcoin):
    """
    Class with all the necessary BlackholeCoin network information based on
    https://github.com/blackholecoin/blackholecoin-master/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'diamond'
    symbols = ('BHC', )
    seeds = ("148.153.8.154",
             "38.121.61.46",
             "38.123.100.66",
             "148.153.8.50",
             "blackholecoin.io",
             "blackholecoin.com",
             "blackholecoin.org")
    port = 19100

# Has no testnet
