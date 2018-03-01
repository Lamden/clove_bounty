from clove.network.bitcoin import Bitcoin


class Scorecoin(Bitcoin):
    """
    Class with all the necessary Scorecoin network information based on
    https://github.com/marksteven2017/Scorecoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'scorecoin'
    symbols = ('SCORE', )
    seeds = ("scorecoin.net")
    port = 17075

# no testnet
