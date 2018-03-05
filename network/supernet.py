from clove.network.bitcoin import Bitcoin


class SuperNET(Bitcoin):
    """
    Class with all the necessary  SuperNET (UNITY) network information based on
    https://github.com/SuperNETorg/komodo/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'supernet'
    symbols = ('UNITY', )
    seeds = ('seeds.komodoplatform.com', 'seeds.komodo.mewhub.com', )
    port = 7770
    message_start = b'\xf9\xee\xe4\x8d'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 188
    }
