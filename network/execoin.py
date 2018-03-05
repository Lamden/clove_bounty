from clove.network.bitcoin import Bitcoin


class Execoin(Bitcoin):
    """
    Class with all the necessary Execoin network information based on
    https://github.com/execoin/execoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'execoin'
    symbols = ('EXE', )
    seeds = ("dnsseed.execoin.net", )
    port = 9989
    message_start = b'\xfa\xbf\xb5\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 161
    }


class ExecoinTestNet(Execoin):
    """
    Class with all the necessary Execoin testing network information based on
    https://github.com/execoin/execoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-execoin'
    seeds = ("testnet-seed.execoin.net", )
    port = 19989
    message_start = b'exec'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
