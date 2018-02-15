from clove.network.bitcoin import Bitcoin


class SoonCoin(Bitcoin):
    """
    Class with all the necessary SoonCoin network information based on
    https://github.com/SoonCoin/Sooncoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'sooncoin'
    symbols = ('SOON', )
    seeds = ("93.157.4.11","192.169.6.169")
    port = 22221

# no testnet