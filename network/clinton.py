from clove.network.bitcoin import Bitcoin


class Clinton(Bitcoin):
    """
    Class with all the necessary Clinton network information based on
    https://github.com/abougadibou/clinton-source/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'clinton'
    symbols = ('CLINT', )
    seeds = ("will.52.207.247.50",
             "bill.54.152.47.236")
    port = 6779
    message_start = b'\x4f\x32\x96\xaa'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 168
    }

# no testnet
