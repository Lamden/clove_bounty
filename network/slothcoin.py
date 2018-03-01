from clove.network.bitcoin import Bitcoin


class Slothcoin(Bitcoin):
    """
    Class with all the necessary Slothcoin (SLOTH) network information based on
    https://github.com/FibaX/Slothcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'slothcoin'
    symbols = ('SLOTH', )
    nodes = ('80.112.144.8', '82.139.127.205', '80.112.172.234',
             '173.209.34.107', '198.23.161.59')
    port = 5107
    message_start = b'\xf9\xbe\xbb\xd2'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }


class SlothcoinTestNet(Slothcoin):
    """
    Class with all the necessary Slothcoin (SLOTH) testing network information based on
    https://github.com/FibaX/Slothcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-slothcoin'
    nodes = ('80.112.144.8', '82.139.127.205', '80.112.172.234',
             '173.209.34.107', '198.23.161.59')
    port = 15107
    message_start = b'\x0b\x11\xbb\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 127,
        'SCRIPT_ADDR': 130,
        'SECRET_KEY': 255
    }
