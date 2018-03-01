from clove.network.bitcoin import Bitcoin


class Polis(Bitcoin):
    """
    Class with all the necessary Polis network information based on
    https://github.com/polispay/polis/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'polis'
    symbols = ('POLIS', )
    seeds = ("node1.polispay.org",
             "node2.polispay.org",
             "node3.polispay.org")
    port = 24126

# no testnet
