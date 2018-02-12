from clove.network.bitcoin import Bitcoin


class InflationCoin(Bitcoin):
    """
    Class with all the necessary InflationCoin network information based on
    https://github.com/inflationcoin/inflationcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'inflationcoin'
    symbols = ('IFLT', )
    seeds = ("45.42.189.71","45.42.189.111")
    port = 11370


# Has no testnet
	
	