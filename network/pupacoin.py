from clove.network.bitcoin import Bitcoin


class PupaCoin(Bitcoin):
    """
    Class with all the necessary PupaCoin network information based on
    https://github.com/pupac/pupa/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'pupacoin'
    symbols = ('PUPA', )
    seeds = ("213.169.33.11")
    port = 6811
    message_start = b'\xee\x17\xea\xcb'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 183
    }


class PupaCoinTestNet(PupaCoin):
    """
    Class with all the necessary PupaCoin testing network information based on
    https://github.com/pupac/pupa/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-pupacoin'
    seeds = ("test1.PupaCoin.pw")
    port = 16811
    message_start = b'\xa7\x41\xae\x7c'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
