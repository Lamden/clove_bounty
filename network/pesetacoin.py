from clove.network.bitcoin import Bitcoin


class Pesetacoin(Bitcoin):
    """
    Class with all the necessary Pesetacoin (PTC) network information based on
    https://github.com/FundacionPesetacoin/Pesetacoin-0.9.1-Oficial/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'pesetacoin'
    symbols = ('PTC', )
    seeds = ('dnsseed.pesetacoin.info', )
    port = 16639


class TerracoinTestNet(Pesetacoin):
    """
    Class with all the necessary Pesetacoin (PTC) testing network information based on
    https://github.com/FundacionPesetacoin/Pesetacoin-0.9.1-Oficial/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-pesetacoin'
    seeds = ('test-seed.pesetachain.info', )
    port = 26339
