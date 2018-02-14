from clove.network.bitcoin import Bitcoin


class Checkcoin(Bitcoin):
    """
    Class with all the necessary Checkcoin network information based on
    https://github.com/Checkcoin/checkcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'checkcoin'
    symbols = ('CKC', )
    seeds = ("dnsseed1.checkcoin.cc",
             "dnsseed2.checkcoin.cc",
             "dnsseed3.checkcoin.cc",
             "dnsseed4.checkcoin.cc",
             "dnsseed5.checkcoin.cc",
             "dnsseed6.checkcoin.cc",
             "dnsseed7.checkcoin.cc",
             "dnsseed8.checkcoin.cc")
    port = 11070

# Has no testnet