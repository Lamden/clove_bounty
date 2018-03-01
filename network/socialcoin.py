
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
    message_start = b'\xee\x64\xe3\x1d'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 191
    }


class SocialCoinTestNet(SocialCoin):
    """
    Class with all the necessary SOCC testing network information based on
    http://www.github.com/SocialCoinNetwk/SocialCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-socialcoin'
    seeds = ()
    port = 28645
