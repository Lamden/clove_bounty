from clove.network.bitcoin import Bitcoin


class JokerCoin(Bitcoin):
    """
    Class with all the necessary JokerCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'jokercoin'
    symbols = ('JOK', )
    nodes = ("45.55.83.96", )
    port = 32880
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }

# No testnet
