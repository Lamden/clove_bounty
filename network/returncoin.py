from clove.network.bitcoin import Bitcoin


class ReturnCoin(Bitcoin):
    """
    Class with all the necessary ReturnCoin network information based on
    https://github.com/ReturnCoin/ReturnCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'returncoin'
    symbols = ('RNC', )
    seeds = ("37.97.135.16")
    port = 60144

# no testnet
