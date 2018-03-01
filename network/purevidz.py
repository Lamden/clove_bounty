
from clove.network.bitcoin import Bitcoin


class PureVidz(Bitcoin):
    """
    Class with all the necessary VIDZ network information based on
    http://www.github.com/purevidz/vidzcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'purevidz'
    symbols = ('VIDZ', )
    seeds = ('163.172.70.91',)
    port = 3818
    message_start = b'\xe4\x15\x53\x11'
    base58_prefixes = {
        'PUBKEY_ADDR': 71,
        'SCRIPT_ADDR': 75,
        'SECRET_KEY': 153
    }


class PureVidzTestNet(PureVidz):
    """
    Class with all the necessary VIDZ testing network information based on
    http://www.github.com/purevidz/vidzcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-purevidz                '
    seeds = ()
    port = 3918
    message_start = b'\xec\xa1\xb2\x01'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
