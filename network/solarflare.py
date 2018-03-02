from clove.network.bitcoin import Bitcoin


class Solarflarecoin(Bitcoin):
    """
    Class with all the necessary Solarflarecoin network information based on
    https://github.com/solarflareproject/solarflarecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Solarflarecoin'
    symbols = ('SFC', )
    seeds = ("54.152.17.29")
    port = 12387


# Has no testnet
