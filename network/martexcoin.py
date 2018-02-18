from clove.network.bitcoin import Bitcoin


class MarteXcoin(Bitcoin):
    """
    Class with all the necessary MarteXcoin network information based on
    https://github.com/martexcoin/martexcoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'martexcoin'
    symbols = ('MXT', )
    seeds = ("seed.martexcoin.org:51315",
             "seed1.martexcoin.org:51315",
             "seed2.martexcoin.org:51315",
             "seed3.martexcoin.org:51315",
             "seed4.martexcoin.org:51315")
    port = 51314
	
# no testnet