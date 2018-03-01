from clove.network.bitcoin import Bitcoin


class GameLeagueCoin(Bitcoin):
    """
    Class with all the necessary GameLeagueCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'gameleaguecoin'
    symbols = ('GML', )
    seeds = ("95.85.38.109", "204.152.209.25")
    port = 20851
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }
