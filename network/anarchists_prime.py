from clove.network.bitcoin import Bitcoin


class AnarchistsPrime(Bitcoin):
    """
    Class with all the necessary  AnarchistsPrime (ACP) network information based on
    https://github.com/AnarchistsPrime/Acp2/tree/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'anarchistsprime'
    symbols = ('ACP', )
    seeds = ('acp.servep2p.com', '159.203.31.42', '139.59.255.88',
             '138.68.143.185', '138.68.14.183', '188.166.175.90', '203.212.152.229')
    port = 11050
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class AnarchistsPrimeTestNet(AnarchistsPrime):
    """
    Class with all the necessary  AnarchistsPrime (ACP) network information based on
    https://github.com/AnarchistsPrime/Acp2/tree/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-anarchistsprime'
    symbols = ('ACP', )
    seeds = ()
    port = 5744
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
