from clove.network.bitcoin import Bitcoin


class PoSWallet(Bitcoin):
    """
    Class with all the necessary PoSWallet network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'poswallet'
    symbols = ('POSW', )
    nodes = ("198.74.56.141",
             "69.164.214.211")
    port = 9175
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }
