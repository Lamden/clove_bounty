from clove.network.bitcoin import Bitcoin


class Tittiecoin(Bitcoin):
    """
    Class with all the necessary TTC network information based on
    https://www.github.com/tittiecoin/tittiecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'tittiecoin'
    symbols = ('TTC', )
    seeds = (
        '178.62.32.188',
        '178.62.32.202',
    )
    port = 8007
    message_start = b'\xd9\xfa\xac\xb3'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 193
    }


class TittieTestNet(Tittiecoin):
    """
    Class with all the necessary TTC testing network information based on
    https://github.com/tittiecoin/tittiecoin/blob/master/src/protocol.h
    (date of access: 02/12/2018)
    """
    name = 'test-tittiecoin'
    seeds = ()
    port = 19117
