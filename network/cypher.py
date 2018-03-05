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
