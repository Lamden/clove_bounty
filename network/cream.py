
from clove.network.bitcoin import Bitcoin


class Cream(Bitcoin):
    """
    Class with all the necessary CRM network information based on
    http://www.github.com/creamcoin/CREAM-cryptocurrency/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'cream'
    symbols = ('CRM', )
    nodes = ('94.176.236.41', '109.235.65.83', '185.69.53.42',
             '91.92.136.100', '91.92.136.99', '185.177.59.7')
    port = 36066
    message_start = b'\x22\xe4\xc3\x14'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 155
    }


class CreamTestNet(Cream):
    """
    Class with all the necessary CRM testing network information based on
    http://www.github.com/creamcoin/CREAM-cryptocurrency/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-cream'
    seeds = ()
    port = 16066
    message_start = b'\xed\xc6\xfe\x20'
    base58_prefixes = {
        'PUBKEY_ADDR': 88,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
