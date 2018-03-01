
from clove.network.bitcoin import Bitcoin


class Megacoin(Bitcoin):
    """
    Class with all the necessary MEC network information based on
    http://www.github.com/LIMXTEC/Megacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'megacoin'
    symbols = ('MEC', )
    seeds = ('dnsseed.megacoin.in', )
    port = 7951
    message_start = b'\xed\xe0\xe4\xee'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }


class MegacoinTestNet(Megacoin):
    """
    Class with all the necessary MEC testing network information based on
    http://www.github.com/LIMXTEC/Megacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-megacoin'
    seeds = ('testnet-seed.ltc.xurious.com', 'dnsseed.wemine-testnet.com')
    port = 17951
    message_start = b'\xfd\xf0\xf4\xfe'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
