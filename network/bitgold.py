from clove.network.bitcoin import Bitcoin


class bitGold(Bitcoin):
    """
    Class with all the necessary bitGold network information based on
    https://github.com/Bit-Gold/BitG/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'bitgold'
    symbols = ('BITGOLD', )
    seeds = ("dnsseed.BitGold.su",
             "dnsseed.BitGold.ru",
             "dnsseed.novaco.in")
    port = 5772
