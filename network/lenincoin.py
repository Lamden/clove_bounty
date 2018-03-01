from clove.network.bitcoin import Bitcoin


class LeninCoin(Bitcoin):
    """
    Class with all the necessary LeninCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'lenincoin'
    symbols = ('LENIN', )
    seeds = ("kicks.servep2p.com")
    port = 10157
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }

# no testnet
