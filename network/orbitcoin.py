from clove.network.bitcoin import Bitcoin


class Orbitcoin(Bitcoin):
    """
    Class with all the necessary Orbitcoin network information based on
    https://github.com/Orbitcoin/Orbitcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'orbitcoin'
    symbols = ('ORB', )
    seeds = ("seed0.phoenixcoin.org",
             "seed1.phoenixcoin.org")
    port = 15298
