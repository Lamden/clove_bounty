from clove.network.bitcoin import Bitcoin


class CrevaCoin(Bitcoin):
    """
    Class with all the necessary CrevaCoin network information based on
    https://github.com/crevacoin/creva/blob/master/crevacoin_source/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'crevacoin'
    symbols = ('CREVA', )
    seeds = ("123.57.60.128")
    port = 22440
    message_start = b'\xfe\xd2\xb1\xda'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }


class CrevaCoinTestNet(CrevaCoin):
    """
    Class with all the necessary CrevaCoin testing network information based on
    https://github.com/crevacoin/creva/blob/master/crevacoin_source/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-crevacoin'
    seeds = ("23.23.186.131")
    port = 22441
