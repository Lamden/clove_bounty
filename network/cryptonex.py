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


class CryptonexTestNet(Cryptonex):
    """
    Class with all the necessary Cryptonex CNX testing network information based on
    https://github.com/Cryptonex/source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-cryptonex'
    seeds = ()
    port = 30863
