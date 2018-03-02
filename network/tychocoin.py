from clove.network.bitcoin import Bitcoin


class Tychocoin(Bitcoin):
    """
    Class with all the necessary Tychocoin network information based on
    https://github.com/tychocoin2017/tychocoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'tychocoin'
    symbols = ('TYCHO', )
    nodes = ("50.63.164.183", )
    port = 9333
    message_start = b'\xc3\xd2\xd1\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 193
    }


class TychocoinTestNet(Tychocoin):
    """
    Class with all the necessary Tychocoin testing network information based on
    https://github.com/tychocoin2017/tychocoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-tychocoin'
    nodes = ("50.63.164.183", )
    port = 19333
    message_start = b'\xd2\xb3\xa4\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
