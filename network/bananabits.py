from clove.network.bitcoin import Bitcoin


class BananaBits(Bitcoin):
    """
    Class with all the necessary BananaBits network information based on
    https://github.com/bananabits/bananabits/blob/master/src/chainparams.cpp
    (date of access: 02/13/2018)
    """
    name = 'bananabits'
    symbols = ('NANAS', )
    seeds = ("seed.bananabits.website")
    port = 31341

# Has no testnet
