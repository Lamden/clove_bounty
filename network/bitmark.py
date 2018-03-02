from clove.network.bitcoin import Bitcoin


class Bitmark(Bitcoin):
    """
    Class with all the necessary Bitmark network information based on
    https://github.com/project-bitmark/bitmark/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitmark'
    symbols = ('BTM', )
    seeds = ("biji.bitmark.one",
             "shido.bitmark.one",
             "ra.zmark.org",
             "shiba.zmark.org",
             "btmk.zmark.org",
             "btmk.bitmark.guru",
             "da.bitmark.guru",
             "da.bitmark.mx",
             "btm.zmark.org")
    port = 9265
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 85,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 213
    }


class BitmarkTestNet(Bitmark):
    """
    Class with all the necessary Bitmark testing network information based on
    https://github.com/project-bitmark/bitmark/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-bitmark'
    seeds = ("test.bitmark.co", )
    port = 19265
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 130,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 258
    }
