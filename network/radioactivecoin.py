from clove.network.bitcoin import Bitcoin


class Radioactivecoin(Bitcoin):
    """
    Class with all the necessary Radioactivecoin network information based on
    https://github.com/CryptoBubble/radioactivecoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'radioactivecoin'
    symbols = ('RAD', )
    seeds = ("162.250.125.26")
    port = 23555
    message_start = b'\xd9\xf6\xe7\xd5'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 6,
        'SECRET_KEY': 163
    }

# no testnet
