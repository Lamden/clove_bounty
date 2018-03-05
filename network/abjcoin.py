from clove.network.bitcoin import Bitcoin


class Abjcoin(Bitcoin):
    """
    Class with all the necessary  Abjcoin (ABJ) network information based on
    https://github.com/abjcoinblockchain/Abjcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'abjcoin'
    symbols = ('ABJ', )
    nodes = ('209.188.21.177', '199.188.207.212', )
    port = 29303
    message_start = b'\x22\x3d\x04\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 163
    }
