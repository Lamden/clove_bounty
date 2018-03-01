
from clove.network.bitcoin import Bitcoin


class QubitCoin(Bitcoin):
    """
    Class with all the necessary Q2C network information based on
    http://www.github.com/willowrose/QubitCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'qubitcoin'
    symbols = ('Q2C', )
    seeds = ('q2c1.ignorelist.com', 'q2c2.ignorelist.com',
             'q2c3.ignorelist.com', 'q2c4.ignorelist.com')
    port = 7788
    message_start = b'\xfe\xa5\x03\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 9,
        'SECRET_KEY': 224
    }


class QubitCoinTestNet(QubitCoin):
    """
    Class with all the necessary Q2C testing network information based on
    http://www.github.com/willowrose/QubitCoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-qubitcoin'
    seeds = ()
    port = 11788
    message_start = b'\x01\x1A\x39\xF7'
    base58_prefixes = {
        'PUBKEY_ADDR': 119,
        'SCRIPT_ADDR': 199,
        'SECRET_KEY': 239
    }
