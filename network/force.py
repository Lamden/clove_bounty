from clove.network.bitcoin import Bitcoin


class Force(Bitcoin):
    """
    Class with all the necessary Force (FOR) network information based on
    https://github.com/forceunited/force/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'force'
    symbols = ('FOR', )
    seeds = ('94.130.107.201', '45.77.201.147')
    port = 37246
    message_start = b'\xf1\xec\xa1\xc7'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
