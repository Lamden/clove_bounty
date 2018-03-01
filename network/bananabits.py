from clove.network.bitcoin import Bitcoin


class BananaBits(Bitcoin):
    """
    Class with all the necessary BananaBits network information based on
    https://github.com/bananabits/bananabits/blob/master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'bananabits'
    symbols = ('NANAS', )
    seeds = ("seed.bananabits.website", )
    port = 31341
    message_start = b'\x1f\xcd\x2d\x3a'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# Has no testnet
