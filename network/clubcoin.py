
from clove.network.bitcoin import Bitcoin


class ClubCoin(Bitcoin):
    """
    Class with all the necessary CLUB network information based on
    http://www.github.com/BitClubDev/ClubCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'clubcoin'
    symbols = ('CLUB', )
    seeds = ('seed1.clubcoin.io', 'seed2.clubcoin.io',
             'seed3.clubcoin.io', 'seed4.clubcoin.io', 'seed5.clubcoin.io')
    port = 18114


class ClubCoinTestNet(ClubCoin):
    """
    Class with all the necessary CLUB testing network information based on
    http://www.github.com/BitClubDev/ClubCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-clubcoin'
    seeds = ()
    port = 28114
