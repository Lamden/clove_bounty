from clove.network.bitcoin import Bitcoin


class BlueCoin(Bitcoin):
    """
    Class with all the necessary BLU network information based on
    https://github.com/bluecoiner/bluecoin-new/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'bluecoin'
    symbols = ('BLU', )
    seeds = ()
    port = 27104
    message_start = b'\xf3\xf2\xae\xad'
    base58_prefixes = {
        'PUBKEY_ADDR': 26,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 176
    }


class BlueCoinTestNet(BlueCoin):
    """
    Class with all the necessary BLU testing network information based on
    https://github.com/bluecoiner/bluecoin-new/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-bluecoin'
    seeds = ()
    port = 17104
    message_start = b'\xfe\xf5\xab\xaa'
    base58_prefixes = {
        'PUBKEY_ADDR': 36,
        'SCRIPT_ADDR': 38,
        'SECRET_KEY': 239
    }
