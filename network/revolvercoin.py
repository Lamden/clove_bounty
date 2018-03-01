
from clove.network.bitcoin import Bitcoin


class RevolverCoin(Bitcoin):
    """
    Class with all the necessary XRE network information based on
    https://github.com/revolvercoin/revolvercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'revolvercoin'
    symbols = ('XRE', )
    seeds = ()
    port = 8777
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class RevolverCoinTestNet(RevolverCoin):
    """
    Class with all the necessary XRE testing network information based on
    https://github.com/revolvercoin/revolvercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-revolvercoin'
    seeds = ()
    port = 18777
    message_start = b'\x0b\x11\x09\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
