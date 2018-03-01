from clove.network.bitcoin import Bitcoin


class Era(Bitcoin):
    """
    Class with all the necessary  Era (ERA) network information based on
    https://github.com/cryptofun/blas/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'era'
    symbols = ('ERA', )
    nodes = ('216.144.230.95', )
    port = 14442
    message_start = b'\xea\x11\x7a\xcc'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 154
    }


class EraTestNet(Era):
    """
    Class with all the necessary  Era (ERA) network information based on
    https://github.com/cryptofun/blas/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-era'
    symbols = ('ERA', )
    nodes = ('216.144.230.95', )
    port = 24442
    message_start = b'\xa7\x41\xae\x7c'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
