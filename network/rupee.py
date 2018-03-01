
from clove.network.bitcoin import Bitcoin


class Rupee(Bitcoin):
    """
    Class with all the necessary RUP network information based on
    http://www.github.com/rupeedigitalassets/RUPEE/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'rupee'
    symbols = ('RUP', )
    seeds = ('165.227.51.103', '104.236.195.94', '138.197.133.4')
    port = 10459
    message_start = b'\x3b\x69\xde\xd4'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 188
    }


class RupeeTestNet(Rupee):
    """
    Class with all the necessary RUP testing network information based on
    http://www.github.com/rupeedigitalassets/RUPEE/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-rupee'
    seeds = ()
    port = 20459
