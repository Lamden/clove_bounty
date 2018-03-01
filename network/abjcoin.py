from clove.network.bitcoin import Bitcoin


class Abjcoin(Bitcoin):
    """
    Class with all the necessary  Abjcoin (ABJ) network information based on
    https://github.com/abjcoinblockchain/Abjcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'abjcoin'
    symbols = ('ABJ', )
    seeds = ('209.188.21.177', '199.188.207.212')
    port = 29303
    message_start = b'\x22\x3d\x04\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 163
    }


class AbjcoinTestNet(Abjcoin):
    """
    Class with all the necessary  Abjcoin (ABJ) network information based on
    https://github.com/abjcoinblockchain/Abjcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-abjcoin'
    symbols = ('ABJ', )
    seeds = ()
    port = 39303
    message_start = b'\x2d\x27\x8e\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
