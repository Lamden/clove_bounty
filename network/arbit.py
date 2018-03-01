
from clove.network.bitcoin import Bitcoin


class Arbit(Bitcoin):
    """
    Class with all the necessary ARB network information based on
    https://github.com/arbitcoin/arbit/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'arbit'
    symbols = ('ARB', )
    seeds = ('162.243.203.211', '178.62.56.172')
    port = 31930
    message_start = b'\xe3\xa7\x7c\x0e'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 151
    }


class ArbitTestNet(Arbit):
    """
    Class with all the necessary ARB testing network information based on
    https://github.com/arbitcoin/arbit/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-arbit'
    seeds = ()
    port = 31914
    message_start = b'\xad\xf1\xc2\xaf'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
