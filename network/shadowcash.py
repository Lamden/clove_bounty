from clove.network.bitcoin import Bitcoin


class ShadowCash(Bitcoin):
    """
    Class with all the necessary ShadowCash (SDC) network information based on
    https://github.com/shadowproject/shadow/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'shadowcash'
    symbols = ('SDC', )
    seeds = ('seed.shadow.cash', 'seed2.shadow.cash', 'seed3.shadow.cash',
             'seed4.shadow.cash', 'seed.shadowproject.io', 'seed.shadowchain.info')
    port = 51737
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }

# no testnet
