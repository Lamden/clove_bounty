
from clove.network.bitcoin import Bitcoin


class DeutscheeMark(Bitcoin):
    """
    Class with all the necessary DEM network information based on
    http://www.github.com/emarkproject/eMark/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'deutsche-emark'
    symbols = ('DEM', )
    seeds = ('seed.deutsche-emark.de', )
    port = 5556
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 181
    }


class DeutscheeMarkTestNet(DeutscheeMark):
    """
    Class with all the necessary DEM testing network information based on
    http://www.github.com/emarkproject/eMark/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-deutsche-emark'
    seeds = ()
    port = 15556
    message_start = b'\xfe\xc3\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
