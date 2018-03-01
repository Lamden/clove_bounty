from clove.network.bitcoin import Bitcoin


class LemonCoin(Bitcoin):
    """
    Class with all the necessary LemonCoin network information based on
    https://github.com/lemoncoin-project/lemoncoin/blob/1.0/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'lemoncoin'
    symbols = ('LEMON', )
    seeds = ("45.32.180.199")
    port = 22331
    message_start = b'\xa8\xf0\xc3\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 33,
        'SECRET_KEY': 176
    }

# no testnet
