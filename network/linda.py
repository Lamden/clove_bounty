from clove.network.bitcoin import Bitcoin


class Linda(Bitcoin):
    """
    Class with all the necessary LINDA network information based on
    https://github.com/lindacoin/linda/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'linda'
    symbols = ('LINDA', )
    seeds = ()
    port = 33820
    message_start = b'\x9c\xd3\x17\x01'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }


class LindaTestNet(Linda):
    """
    Class with all the necessary LINDA testing network information based on
    https://github.com/lindacoin/linda/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-linda'
    seeds = ()
    port = 28888
    message_start = b'\xce\xf2\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 187,
        'SECRET_KEY': 239
    }
