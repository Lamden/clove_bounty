from clove.network.bitcoin import Bitcoin


class Slimcoin(Bitcoin):
    """
    Class with all the necessary Slimcoin network information based on
    https://github.com/slimcoin-project/Slimcoin/blob/slimcoin/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'slimcoin'
    symbols = ('SLM', )
    seeds = ("dnsseed.slimcoinpool.com",
             "dnsseed.furiousnomad.com",
             "dnsseed.shitcoinrapist.club")
    port = 41682
	
