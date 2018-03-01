from clove.network.bitcoin import Bitcoin


class Atmos(Bitcoin):
    """
    Class with all the necessary  Atmos (ATMS) network information based on
    https://github.com/asphyxiating/atmostemp/blob/master/atmos-master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'atmos'
    symbols = ('ATMS', )
    seeds = ('212.129.37.112')
    port = 9834
    message_start = b'\xc3\xa0\x08\x12'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }


class AtmosTestNet(Atmos):
    """
    Class with all the necessary  Atmos (ATMS) network information based on
    https://github.com/asphyxiating/atmostemp/blob/master/atmos-master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-atmos'
    symbols = ('ATMS', )
    seeds = ()
    port = 9835
    message_start = b'\xa3\xb0\x18\x22'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
