from clove.network.bitcoin import Bitcoin


class BetaCoin(Bitcoin):
    """
    Class with all the necessary BetaCoin network information based on
    https://github.com/BetaCoinDev/betacoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'betacoin'
    symbols = ('BET', )
    seeds = ("seed1.betacoin.org",
             "seed2.betacoin.org",
             "seed3.betacoin.org",
             "seed4.betacoin.org",
             "seed5.betacoin.org",
             "seed6.betacoin.org")
    port = 32333


class BetaCoinTestNet(BetaCoin):
    """
    Class with all the necessary BetaCoin testing network information based on
    https://github.com/BetaCoinDev/betacoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-betacoin'
    seeds = ("xjo-test1.twilightparadox.com")
    port = 26783
