from clove.network.bitcoin import Bitcoin


class EACoin(Bitcoin):
    """
    Class with all the necessary EA Coin (EAG) network information based on
    https://github.com/eacoin-project/eacore/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'eacoin'
    symbols = ('EAG', )
    seeds = ('eaglive.co', )
    port = 28635
    message_start = b'\xc4\xb1\xc6\x4c'
    base58_prefixes = {
        'PUBKEY_ADDR': 32,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 192
    }

# no testnet
