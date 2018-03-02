
from clove.network.bitcoin import Bitcoin


class Masternodecoin(Bitcoin):
    """
    Class with all the necessary MTNC network information based on
    http://www.github.com/masternodecoin/masternodecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'masternodecoin'
    symbols = ('MTNC', )
    nodes = ('47.52.46.158', '23.247.2.51', )
    port = 10086
    message_start = b'\xd5\xce\x8c\x5e'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }


class MasternodecoinTestNet(Masternodecoin):
    """
    Class with all the necessary MTNC testing network information based on
    http://www.github.com/masternodecoin/masternodecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-masternodecoin'
    seeds = ()
    port = 11111
    message_start = b'\xf2\xae\xe7\xe4'
    base58_prefixes = {
        'PUBKEY_ADDR': 97,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
