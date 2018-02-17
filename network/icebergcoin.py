from clove.network.bitcoin import Bitcoin


class IcebergCoin(Bitcoin):
    """
    Class with all the necessary IcebergCoin network information based on
    https://github.com/ICBcoin/icebergcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'IcebergCoin'
    symbols = ('ICB', )
    seeds = ("seed.icebergco.in",
             "seed.shurpool.com",
             "31.220.50.78",
             "embi.zapto.org")
    port = 20703
	
# No testnet
