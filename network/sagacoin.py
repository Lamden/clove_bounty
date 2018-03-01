
from clove.network.bitcoin import Bitcoin


class SagaCoin(Bitcoin):
    """
    Class with all the necessary SAGA network information based on
    http://www.github.com/sagacrypto/SagaCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'sagacoin'
    symbols = ('SAGA', )
    seeds = ('node1.sagacoin.net', 'node2.sagacoin.net', 'node3.sagacoin.net')
    port = 48744
    message_start = b'\xaa\xa3\xb2\xc4'
    base58_prefixes = {
        'PUBKEY_ADDR': 125,
        'SCRIPT_ADDR': 44,
        'SECRET_KEY': 142
    }


class SagaCoinTestNet(SagaCoin):
    """
    Class with all the necessary SAGA testing network information based on
    http://www.github.com/sagacrypto/SagaCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-sagacoin'
    seeds = ()
    port = 45544
    message_start = b'\xa1\x79\xa4\xa2'
    base58_prefixes = {
        'PUBKEY_ADDR': 61,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 229
    }
