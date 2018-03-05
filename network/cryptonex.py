from clove.network.bitcoin import Bitcoin


class Cryptonex(Bitcoin):
    """
    Class with all the necessary Cryptonex CNX network information based on
    https://github.com/Cryptonex/source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'cryptonex'
    symbols = ('CNX', )
    seeds = (
        'node-london.cryptonex.org', 'node-frankfurt.cryptonex.org', 'node-amsterdam.cryptonex.org',
        'node-toronto.cryptonex.org', 'node-singapore.cryptonex.org', 'node-paris.cryptonex.org',
        'node-bangalore.cryptonex.org'
    )
    port = 20863
    message_start = b'\x18\xe4\x82\xa0'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 166
    }
