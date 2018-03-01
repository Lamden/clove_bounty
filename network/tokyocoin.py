from clove.network.bitcoin import Bitcoin


class Tokyocoin(Bitcoin):
    """
    Class with all the necessary TOKC network information based on
    https://github.com/tokyocoindev/tokyocoinsrc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'tokyocoin'
    symbols = ('TOKC', )
    seeds = (
        'node.tokyocoin.info',
    )
    port = 23517
    message_start = b'\x00\x5a\xab\x1e'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 193
    }


class TokyocoinTestNet(Tokyocoin):
    """
    Class with all the necessary TOKC testing network information based on
    https://github.com/tokyocoindev/tokyocoinsrc/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-tokyocoin'
    seeds = ()
    port = 33517
