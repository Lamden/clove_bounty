from clove.network.bitcoin import Bitcoin


class REGAcoin(Bitcoin):
    """
    Class with all the necessary REGAcoin (REGA) network information based on
    https://github.com/REGAcoin/REGA/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'regacoin'
    symbols = ('REGA', )
    seeds = ('seed3.cryptolife.net', 'electrum3.cryptolife.net',
             'seed4.cryptolife.net', '51.255.38.250')
    port = 28192
    message_start = b'\xd4\xca\x3f\xec'
    base58_prefixes = {
        'PUBKEY_ADDR': 61,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 189
    }

# no testnet
