from clove.network.bitcoin import Bitcoin


class Alqo(Bitcoin):
    """
    Class with all the necessary  Alqo (ALQO) network information based on
    https://github.com/ALQOCRYPTO/ALQO/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'alqo'
    symbols = ('ALQO', )
    seeds = ('85.25.138.64', '85.25.251.198', '85.25.251.199', '80.209.227.9', '80.209.228.189', '80.209.228.190',
             '80.209.228.191', '80.209.228.192', '80.209.228.193', '80.209.228.194', '80.209.228.195', '80.209.228.196',
             '80.209.228.197')
    port = 55500
    message_start = b'\x94\x04\x15\x14'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 16,
        'SECRET_KEY': 193
    }


class AlqoTestNet(Alqo):
    """
    Class with all the necessary  Alqo (ALQO) network information based on
    https://github.com/ALQOCRYPTO/ALQO/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-alqo'
    symbols = ('ALQO', )
    seeds = ('85.25.138.64', '85.25.251.198', '85.25.251.199', '80.209.227.9', '80.209.228.189', '80.209.228.190',
             '80.209.228.191', '80.209.228.192', '80.209.228.193', '80.209.228.194', '80.209.228.195', '80.209.228.196',
             '80.209.228.197')
    port = 55600
    message_start = b'\x64\x44\x65\x54'
    base58_prefixes = {
        'PUBKEY_ADDR': 83,
        'SCRIPT_ADDR': 18,
        'SECRET_KEY': 193
    }
