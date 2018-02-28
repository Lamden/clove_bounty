from clove.network.bitcoin import Bitcoin


class Bitgem(Bitcoin):
    """
    Class with all the necessary Bitgem network information based on
    https://github.com/bitgem/bitgem/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Bitgem'
    symbols = ('BTG', )
    seeds = ("bitgem.us", "seed.bitgem.us")
    port = 7692


# Has no Testnet
