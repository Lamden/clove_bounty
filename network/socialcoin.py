
from clove.network.bitcoin import Bitcoin


class SocialCoin(Bitcoin):
    """
    Class with all the necessary SOCC network information based on
    http://www.github.com/SocialCoinNetwk/SocialCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'socialcoin'
    symbols = ('SOCC', )
    seeds = ('13.59.61.11',)
    port = 18645


class SocialCoinTestNet(SocialCoin):
    """
    Class with all the necessary SOCC testing network information based on
    http://www.github.com/SocialCoinNetwk/SocialCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-socialcoin'
    seeds = ()
    port = 28645
