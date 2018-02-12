from clove.network.bitcoin import Bitcoin


class Capricoin(Bitcoin):
    """
    Class with all the necessary Capricoin network information based on
    https://github.com/capricoinofficial/capricoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Capricoin'
    symbols = ('CPC', )
    seeds =  ("seed1.capricoin.org",
		      "seed2.capricoin.org",
		      "seed3.capricoin.org",
		      "seed4.capricoin.org",
		      "seed5.capricoin.org",
		      "seed6.capricoin.org",
		      "seed7.capricoin.org",
		      "seed8.capricoin.org",
		      "seed9.capricoin.org",
		      "seed10.capricoin.org",
		      "seed11.capricoin.org",
		      "seed12.capricoin.org")
    port = 22714


# Has no Testnet