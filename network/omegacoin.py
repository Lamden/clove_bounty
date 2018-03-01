from clove.network.bitcoin import Bitcoin


class OmegaCoin(Bitcoin):
    """
    Class with all the necessary OmegaCoin network information based on
    https://github.com/omegacoinnetwork/omegacoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'omegacoin'
    symbols = ('OMA', )
    seeds = ("79.137.84.252", "158.69.207.254")
    port = 7777
    message_start = b'\xbf\x0c\x6b\xbd'
    base58_prefixes = {
        'PUBKEY_ADDR': 115,
        'SCRIPT_ADDR': 15,
        'SECRET_KEY': 125
    }


class OmegaCoinTestNet(OmegaCoin):
    """
    Class with all the necessary OmegaCoin testing network information based on
    https://github.com/omegacoinnetwork/omegacoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-omegacoin'
    seeds = ("159.89.101.252",
             "207.154.249.8")
    port = 17777
    message_start = b'\xce\xe2\xca\xff'
    base58_prefixes = {
        'PUBKEY_ADDR': 140,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
