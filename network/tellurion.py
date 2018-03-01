from clove.network.bitcoin import Bitcoin


class Tellurion(Bitcoin):
    """
    Class with all the necessary Tellurion network information based on
    https://github.com/telluriondev/tellurion/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'tellurion'
    symbols = ('TELL', )
    seeds = ("seed1.tellurion.co", "seed2.tellurion.co",
             "seed3.tellurion.co", "seed4.tellurion.co",
             "ok1.altcoinsfoundation.com")
    port = 9999


# Has no testnet
