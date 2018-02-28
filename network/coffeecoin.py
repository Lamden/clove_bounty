from clove.network.bitcoin import Bitcoin


class CoffeeCoin(Bitcoin):
    """
    Class with all the necessary CoffeeCoin network information based on
    https://github.com/Orangecoins/Coffecoin-2.0/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'coffeecoin'
    symbols = ('CFC', )
    seeds = ("54.235.70.55", "54.235.244.167")
    port = 16789

# Has no testnet
