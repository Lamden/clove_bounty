from clove.network.bitcoin import Bitcoin


class Neoscoin(Bitcoin):
    """
    Class with all the necessary Neoscoin (NEOS) network information based on
    https://github.com/neoscoin/neos-core/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'neoscoin'
    symbols = ('NEOS', )
    seeds = ('nodes.neoscoin.com')
    port = 29320

# no testnet