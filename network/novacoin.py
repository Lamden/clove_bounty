from clove.network.bitcoin import Bitcoin


class Novacoin(Bitcoin):
    """
    Class with all the necessary Novacoin network information based on
    https://github.com/novacoin-project/novacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Novacoin'
    symbols = ('NVC', )
    seeds = ("dnsseed.novacoin.karelia.pro",
             "dnsseed.novacoin.ru",
             "testseed.novacoin.ru",
             "dnsseed.novaco.in")
    port = 7777


# Has no testnet
