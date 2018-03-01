
from clove.network.bitcoin import Bitcoin


class Greencoin(Bitcoin):
    """
    Class with all the necessary GRE network information based on
    http://www.github.com/greencoin-dev/GreenCoinV2/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'greencoin'
    symbols = ('GRE', )
    seeds = ('149.202.137.169', '81.83.209.224',
             '67.161.120.48', '73.12.235.88', '174.31.114.98')
    port = 11517
    message_start = b'\x05\x22\x53\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 166
    }


class GreencoinTestNet(Greencoin):
    """
    Class with all the necessary GRE testing network information based on
    http://www.github.com/greencoin-dev/GreenCoinV2/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-greencoin'
    seeds = ()
    port = 25713
    message_start = b'\xfe\x0c\x2f\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 240
    }
