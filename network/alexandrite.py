from clove.network.bitcoin import Bitcoin


class Alexandrite(Bitcoin):
    """
    Class with all the necessary Alexandrite network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'alexandrite'
    symbols = ('ALEX', )
    seeds = ("194.135.85.41")
    port = 19531
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }

# Has no testnet
