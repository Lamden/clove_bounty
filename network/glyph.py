from clove.network.bitcoin import Bitcoin


class Glyph(Bitcoin):
    """
    Class with all the necessary Glyph network information based on
    https://github.com/glyphcoin/glyphcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'glyph'
    symbols = ('GLYPH', )
    seeds = ("node.glyphcoin.com", )
    port = 47714
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 15,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 143
    }

# no testnet
