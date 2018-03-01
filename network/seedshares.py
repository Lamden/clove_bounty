from clove.network.bitcoin import Bitcoin


class SeedShares(Bitcoin):
    """
    Class with all the necessary SeedShares network information based on
    https://github.com/SeedShares/SeedShare/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'seedshares'
    symbols = ('SEEDS', )
    seeds = ("107.170.238.71")
    port = 32231
    message_start = b'\xfa\xf2\xef\xb4'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }

# no testnet
