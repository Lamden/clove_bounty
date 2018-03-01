from clove.network.bitcoin import Bitcoin


class Entropycoin(Bitcoin):
    """
    Class with all the necessary Entropycoin network information based on
    https://github.com/etcdev/EntropyCoins/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'entropycoin'
    symbols = ('ENC', )
    seeds = ("seed.entropycoins.com")
    port = 7559
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 161
    }

# no testnet
