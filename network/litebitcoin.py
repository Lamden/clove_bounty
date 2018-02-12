
from clove.network.bitcoin import Bitcoin


class LiteBitcoin(Bitcoin):
    """
    Class with all the necessary LBTC network information based on
    http://www.github.com/litebitcoins/litebitcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'litebitcoin'
    symbols = ('LBTC', )
    seeds = ('litebitcoins.thecryptochat.net',)
    port = 19037


class LiteBitcoinTestNet(LiteBitcoin):
    """
    Class with all the necessary LBTC testing network information based on
    http://www.github.com/litebitcoins/litebitcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-litebitcoin'
    seeds = ()
    port = 19335
