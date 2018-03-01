from clove.network.bitcoin import Bitcoin


class Qbic(Bitcoin):
    """
    Class with all the necessary Qbic (QBIC) network information based on
    https://github.com/qbic-platform/qbic/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'qbic'
    symbols = ('QBIC', )
    seeds = ('seed.qbic.io', )
    port = 17195
    message_start = b'\x1a\xb2\xc3\xd4'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 198
    }


class QbicTestNet(Qbic):
    """
    Class with all the necessary Qbic (QBIC) testing network information based on
    https://github.com/qbic-platform/qbic/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-qbic'
    seeds = ('testnet-dns.qbic.io', )
    port = 18196
    message_start = b'\xd1\x2b\xb3\x7a'
    base58_prefixes = {
        'PUBKEY_ADDR': 112,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 240
    }
