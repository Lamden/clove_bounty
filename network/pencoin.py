from clove.network.bitcoin import Bitcoin


class PenCoin(Bitcoin):
    """
    Class with all the necessary PenCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'pencoin'
    symbols = ('PEN', )
    nodes = ("108.61.103.46", )
    port = 31810
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }

# no testnet
