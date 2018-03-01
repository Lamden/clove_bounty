from clove.network.bitcoin import Bitcoin


class GoldPressedLatinum(Bitcoin):
    """
    Class with all the necessary GoldPressedLatinum network information based on
    https://github.com/scificrypto/gold-pressed-latinum/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'goldpressedlatinum'
    symbols = ('GPL', )
    seeds = ("seed.goldpressedlatinum.su", )
    port = 23635
    message_start = b'\xcd\xf2\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 140,
        'SECRET_KEY': 163
    }


# Has no testnet
