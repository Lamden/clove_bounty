from clove.network.bitcoin import Bitcoin


class Aliencoin(Bitcoin):
    """
    Class with all the necessary Aliencoin network information based on
    https://github.com/Aliencoin2017/aliencoin/blob/master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'Aliencoin'
    symbols = ('ALN', )
    seeds = ("45.32.130.243")
    port = 15424


# Has no testnet
