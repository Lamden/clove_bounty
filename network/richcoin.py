from clove.network.bitcoin import Bitcoin


class RichCoin(Bitcoin):
    """
    Class with all the necessary RichCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'richcoin'
    symbols = ('RICHX', )
    seeds = ("richcoin.us", )
    port = 11777
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }

# no testnet
