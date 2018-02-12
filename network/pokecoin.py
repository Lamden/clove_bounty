from clove.network.bitcoin import Bitcoin


class PokeCoin(Bitcoin):
    """
    Class with all the necessary PokeCoin network information based on
    https://github.com/pokecoindev/pokecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'pokecoin'
    symbols = ('POKE', )
    seeds = ("seed1.pokecoin.trade",
             "seed2.pokecoin.trade",
             "seed3.pokecoin.trade",
             "seed4.pokecoin.trade")
    port = 3333


# Has no testnet
