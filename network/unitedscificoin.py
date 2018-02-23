from clove.network.bitcoin import Bitcoin


class UnitedSciFiCoin(Bitcoin):
    """
    Class with all the necessary UnitedSciFiCoin network information based on
    https://github.com/scificrypto/UnitedSciFiCoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'unitedscificoin'
    symbols = ('SCIFI', )
    seeds = ("dnsseed.unitedscifi.com",
             "pool.unitedscifi.com")
    port = 8454
	
