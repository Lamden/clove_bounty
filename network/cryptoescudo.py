from clove.network.bitcoin import Bitcoin


class CryptoEscudo(Bitcoin):
    """
    Class with all the necessary CryptoEscudo (CESC) network information based on
    https://github.com/Marcdnd/cryptoescudo/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'cryptoescudo'
    symbols = ('CESC', )
    seeds = (
        'seed1.cryptoescudo.org', 'seed2.cryptoescudo.org',
        'seed3.cryptoescudo.org', 'seed4.cryptoescudo.org',
        'seed5.cryptoescudo.org', 'seed6.cryptoescudo.org',
        'seed7.cryptoescudo.org', 'seed8.cryptoescudo.org',
        'seed9.cryptoescudo.org'
    )
    port = 61143
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 88,
        'SECRET_KEY': 156
    }


class CryptoEscudoTestNet(CryptoEscudo):
    """
    Class with all the necessary CryptoEscudo (CESC) testing network information based on
    https://github.com/Marcdnd/cryptoescudo/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-cryptoescudo'
    seeds = ('testseed.cryptoescudo.org', )
    port = 51143
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
