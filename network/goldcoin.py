from clove.network.bitcoin import Bitcoin


class Goldcoin(Bitcoin):
    """
    Class with all the necessary Goldcoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'goldcoin'
    symbols = ('GLD', )
    seeds = ("seed.gldcoin.com", "vps.gldcoin.com")
    port = 8121

# no testnet
