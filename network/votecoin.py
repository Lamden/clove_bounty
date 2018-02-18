from clove.network.bitcoin import Bitcoin


class Votecoin(Bitcoin):
    """
    Class with all the necessary Votecoin (VOT) network information based on
    https://github.com/Tomas-M/VoteCoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'votecoin'
    symbols = ('VOT', )
    seeds = ('dnsseed.votecoin.site')
    port = 8144


class VotecoinTestNet(Votecoin):
    """
    Class with all the necessary Votecoin (VOT) testing network information based on
    https://github.com/Tomas-M/VoteCoin/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-votecoin'
    seeds = ('dnsseed.testnet.z.cash')
    port = 18233
