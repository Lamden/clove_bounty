from clove.network.bitcoin import Bitcoin


class Free_Game_Zone(Bitcoin):
    """
    Class with all the necessary Free Game Zone network information based on
    https://github.com/carlcaleb43/freegamezone-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'free_game_zone'
    symbols = ('FGZ', )
    seeds = ("node.45.32.217.42")
    port = 8999

# no testnet
