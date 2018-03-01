from clove.network.bitcoin import Bitcoin


class Arab_League_Coin(Bitcoin):
    """
    Class with all the necessary Arab_League_Coin network information based on
    https://github.com/arableague/ArabLeagueCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'arab_league_coin'
    symbols = ('ALC', )
    seeds = ("37.59.104.238")
    port = 33612

# no testnet
