from clove.network.bitcoin import Bitcoin


class Astral(Bitcoin):
    """
    Class with all the necessary Astral network information based on
    https://github.com/astralcoindev/ASTRAL/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'astral'
    symbols = ('AST', )
    seeds = ("2.62.25.198")
    port = 96755

# Has no testnet
