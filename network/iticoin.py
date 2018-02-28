from clove.network.bitcoin import Bitcoin


class iTicoin(Bitcoin):
    """
    Class with all the necessary iTicoin network information based on
    https://github.com/sppl/iti/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'iTicoin'
    symbols = ('ITI', )
    seeds = ("seed1.super-ppl.com",
             "seed2.super-ppl.com", "seed3.super-ppl.com")
    port = 42177


# Has no testnet
("seed1.super-ppl.com", "seed2.super-ppl.com", "seed3.super-ppl.com")
