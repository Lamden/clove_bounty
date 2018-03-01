from clove.network.bitcoin import Bitcoin


class GEN(Bitcoin):
    """
    Class with all the necessary G3N (G3N) network information based on
    https://github.com/GenStakeTeam/genstake/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'g3n'
    symbols = ('G3N', )
    seeds = ('genseed.presstab.pw', 'gen.seed.fuzzbawls.pw', 'gen.netcraft.ch', )
    port = 9341
    message_start = b'\xf1\xf7\xf9\xfb'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 52,
        'SECRET_KEY': 166
    }

# no testnet
