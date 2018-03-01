from clove.network.bitcoin import Bitcoin


class GoldPressedLatinum(Bitcoin):
    """
    Class with all the necessary  Gold Pressed Latinum (GPL) network information based on
    https://github.com/scificrypto/Gold-Pressed-Latinum/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'gold_pressed_latinum'
    symbols = ('GPL', )
    seeds = ('seed.goldpressedlatinum.su', )
    port = 23635
    message_start = b'\xcd\xf2\xc0\xef'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 140,
        'SECRET_KEY': 163
    }


# no testnet
