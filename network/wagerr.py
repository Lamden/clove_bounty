from clove.network.bitcoin import Bitcoin


class Wagerr(Bitcoin):
    """
    Class with all the necessary  Wagerr (WGR) network information based on
    https://github.com/wagerr/wagerr/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'wagerr'
    symbols = ('WGR', )
    seeds = ('main.seederv1.wgr.host', 'main.seederv2.wgr.host',
             'main.devseeder1.wgr.host', 'main.devseeder2.wgr.host')
    port = 55002
    message_start = b'\x84\x2d\x61\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 63,
        'SECRET_KEY': 199
    }


class WagerrTestNet(Wagerr):
    """
    Class with all the necessary  Wagerr (WGR) network information based on
    https://github.com/wagerr/wagerr/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-wagerr'
    symbols = ('WGR', )
    seeds = ('test.testseederv1.wgr.host', 'test.testseederv2.wgr.host',
             'test.devseeder1.wgr.host', 'test.devseeder2.wgr.host')
    port = 55004
    message_start = b'\x87\x9e\xd1\x99'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 177
    }
