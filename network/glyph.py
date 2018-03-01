from clove.network.bitcoin import Bitcoin


class Glyph(Bitcoin):
    """
    Class with all the necessary Glyph network information based on
    https://github.com/glyphcoin/glyphcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'glyph'
    symbols = ('GLYPH', )
    seeds = ("node.glyphcoin.com")
    port = 47714

# no testnet
