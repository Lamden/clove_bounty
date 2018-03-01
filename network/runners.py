from clove.network.bitcoin import Bitcoin


class Runners(Bitcoin):
    """
    Class with all the necessary Runners (RUNNERS) network information based on
    https://github.com/runnersdev/runners-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'runners'
    symbols = ('RUNNERS', )
    seeds = ('104.200.67.104')
    port = 20649
    message_start = b'\x45\x98\x4c\x4f'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 188
    }

# no testnet
