from clove.network.bitcoin import Bitcoin


class Bela(Bitcoin):
    """
    Class with all the necessary Bela network information based on
    https://github.com/TheAmbiaFund/Belacoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bela'
    symbols = ('BELA', )
    seeds = ("seed.belacoin.org")
    port = 10554


# Has no testnet
