
from clove.network.bitcoin import Bitcoin


class PepeCoin(Bitcoin):
    """
    Class with all the necessary MEME network information based on
    http://www.github.com/pepeteam/pepecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'pepecoin'
    symbols = ('MEME', )
    seeds = ('seed.kekdaq.com', 'seed.pepecoin.co')
    port = 29377


class PepeCoinTestNet(PepeCoin):
    """
    Class with all the necessary MEME testing network information based on
    http://www.github.com/pepeteam/pepecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-pepecoin'
    seeds = ()
    port = 39377
