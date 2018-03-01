from clove.network.bitcoin import Bitcoin


class Bumbacoin(Bitcoin):
    """
    Class with all the necessary Bumbacoin network information based on
    https://github.com/bumbacoin/bumbacoin2-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Bumbacoin'
    symbols = ('BUMBA', )
    seeds = ("82.211.31.215", "84.200.210.130")
    port = 20222


# Has no Testnet
