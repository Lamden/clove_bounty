from clove.network.bitcoin import Bitcoin


class Phreak(Bitcoin):
    """
    Class with all the necessary Phreak network information based on
    https://github.com/qtvideofilter/streamingcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'phreak'
    symbols = ('PHR', )
    seeds = ("52.26.166.22")
    port = 4744
	
# no testnet