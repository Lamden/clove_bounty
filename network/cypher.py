from clove.network.bitcoin import Bitcoin


class Cypher(Bitcoin):
    """
    Class with all the necessary CYP network information based on
    https://github.com/neworldorder/braveneworld/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cypher'
    symbols = ('CYP', )
    nodes = (
        '54.148.121.237',
    )
    port = 5424
    message_start = b'\x2d\x3f\xa2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 163
    }


class CypherTestNet(Cypher):
    """
    Class with all the necessary CYP testing network information based on
    https://github.com/neworldorder/braveneworld/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-cypher'
    seeds = ()
    nodes = ()
    port = 28224
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
