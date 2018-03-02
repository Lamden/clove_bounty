
from clove.network.bitcoin import Bitcoin


class Unify(Bitcoin):
    """
    Class with all the necessary UNIFY network information based on
    http://www.github.com/SBDomains/unify-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'unify'
    symbols = ('UNIFY', )
    seeds = ('node1.unifycoin.ovh', 'node2.unifycoin.ovh',
             'node3.unifycoin.ovh', 'node1.unifycoin.pl', 'node2.unifycoin.pl', 'node3.unifycoin.pl')
    port = 18649
    message_start = b'\xc4\x47\xf9\xee'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 196
    }


class UnifyTestNet(Unify):
    """
    Class with all the necessary UNIFY testing network information based on
    http://www.github.com/SBDomains/unify-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-unify'
    seeds = ()
    port = 28649
    message_start = b'\xb5\xbb\xdd\x7b'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
