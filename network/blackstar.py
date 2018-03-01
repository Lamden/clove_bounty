from clove.network.bitcoin import Bitcoin


class Blackstar(Bitcoin):
    """
    Class with all the necessary BSTAR network information based on
    https://github.com/bstarcoin/blackstar/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'blackstar'
    symbols = ('BSTAR', )
    seeds = ()
    port = 16878
    message_start = b'\x47\x51\x5a\xb7'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 48,
        'SECRET_KEY': 153
    }


class BlackstarTestNet(Blackstar):
    """
    Class with all the necessary BSTAR testing network information based on
    https://github.com/bstarcoin/blackstar/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-blackstar'
    seeds = ()
    port = 16879
    message_start = b'\x77\x61\x79\x67'
    base58_prefixes = {
        'PUBKEY_ADDR': 135,
        'SCRIPT_ADDR': 208,
        'SECRET_KEY': 249
    }
