from clove.network.bitcoin import Bitcoin


class Moneta(Bitcoin):
    """
    Class with all the necessary Moneta (MONETA) network information based on
    https://github.com/moneta-project/moneta/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'moneta'
    symbols = ('MONETA', )
    nodes = ('95.85.55.13', '188.166.45.174', '178.62.195.161',
             '188.166.92.128', '128.199.38.11')
    port = 10333
    message_start = b'\xc3\xd2\xd1\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }


class MonetaTestNet(Moneta):
    """
    Class with all the necessary Moneta (MONETA) testing network information based on
    https://github.com/moneta-project/moneta/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-moneta'
    seeds = ('testnet-seed.ltc.xurious.com', 'dnsseed.wemine-testnet.com', )
    port = 11333
    message_start = b'\xd1\xb2\xa4\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
