from clove.network.bitcoin import Bitcoin


class Maieuticoin(Bitcoin):
    """
    Class with all the necessary Maieuticoin network information based on
    https://github.com/C2MMXIV/MMXIV/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'maieuticoin'
    symbols = ('MMXIV', )
    seeds = ("dnsseed.mmxivcoin.com")
    port = 11065
	