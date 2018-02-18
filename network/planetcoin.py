from clove.network.bitcoin import Bitcoin


class PlanetCoin(Bitcoin):
    """
    Class with all the necessary PlanetCoin network information based on
    https://github.com/planetcoin/planetcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'planetcoin'
    symbols = ('PLANET', )
    seeds = ("178.62.235.171")
    port = 10410
	
# no testnet