from clove.network.bitcoin import Bitcoin


class Bitstar(Bitcoin):
    """
    Class with all the necessary Bitstar network information based on
    https://github.com/bitstar/bitstar/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Bitstar'
    symbols = ('BITS', )
    seeds = ("seed.bitstarcoin.com", "seed.bitstarcoin.com",
    "seed2.bitstarcoin.com", "seed2.bitstarcoin.com",
    "seed3.bitstarcoin.com", "seed3.bitstarcoin.com",
    "seed4.bitstarcoin.com", "seed4.bitstarcoin.com")
    port = 62123


# Has no Testnet