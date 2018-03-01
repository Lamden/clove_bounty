from clove.network.bitcoin import Bitcoin


class Nerdcoin(Bitcoin):
    """
    Class with all the necessary Nerdcoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/21/2018)
    """
    name = 'nerdcoin'
    symbols = ('NERD', )
    nodes = ("45.55.148.6", )
    port = 31338
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }

# no testnet
