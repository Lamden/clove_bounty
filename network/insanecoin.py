
from clove.network.bitcoin import Bitcoin


class InsaneCoin(Bitcoin):
    """
    Class with all the necessary INSN network information based on
    http://www.github.com/CryptoCoderz/INSN/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'insanecoin'
    symbols = ('INSN', )
    seeds = ('insn.cryptocoderz.com',
             'insane.cryptocoderz.com')
    port = 10255
    message_start = b'\xa4\x3c\x2e\xf9'
    base58_prefixes = {
        'PUBKEY_ADDR': 102,
        'SCRIPT_ADDR': 57,
        'SECRET_KEY': 55
    }


class InsaneCoinTestNet(InsaneCoin):
    """
    Class with all the necessary INSN testing network information based on
    http://www.github.com/CryptoCoderz/INSN/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-insanecoin'
    seeds = ()
    port = 10260
    message_start = b'\x2c\xcc\xc3\xca'
    base58_prefixes = {
        'PUBKEY_ADDR': 103,
        'SCRIPT_ADDR': 39,
        'SECRET_KEY': 63
    }
