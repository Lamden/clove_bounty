
from clove.network.bitcoin import Bitcoin


class SocialSend(Bitcoin):
    """
    Class with all the necessary SEND network information based on
    https://github.com/SocialSend/SocialSend/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'socialsend'
    symbols = ('SEND', )
    seeds = (
        'seeds.send.goldlineit.org',
    )
    port = 50050


class SocialSendTestNet(SocialSend):
    """
    Class with all the necessary SEND testing network information based on
    https://github.com/SocialSend/SocialSend/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-socialsend'
    seeds = ()
    port = 51474
