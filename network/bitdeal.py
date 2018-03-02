from clove.network.bitcoin import Bitcoin


class Bitdeal(Bitcoin):
    """
    Class with all the necessary Bitdeal network information based on
    https://github.com/bitdeal/bitdeal/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitdeal'
    symbols = ('BDL', )
    seeds = ("dnsseed.bitdeal.co.in", )
    port = 9333
    message_start = b'\xfa\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 176
    }

# Has no testnet
