from clove.network.bitcoin import Bitcoin


class Blocknet(Bitcoin):
    """
    Class with all the necessary Blocknet (BLOCK) network information based on
    https://github.com/BlocknetDX/BlockDX/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'blocknet'
    symbols = ('BLOCK', )
    nodes = ('178.62.90.213', '138.197.73.214', '34.235.49.248', )
    port = 41412
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 154
    }


class BlocknetTestNet(Blocknet):
    """
    Class with all the necessary Blocknet (BLOCK) testing network information based on
    https://github.com/BlocknetDX/BlockDX/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-blocknet'
    nodes = ('178.62.90.213', '138.197.73.214', '34.235.49.248', )
    port = 41474
    message_start = b'\x45\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
