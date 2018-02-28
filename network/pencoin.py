from clove.network.bitcoin import Bitcoin


class PenCoin(Bitcoin):
    """
    Class with all the necessary PenCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'pencoin'
    symbols = ('PEN', )
    seeds = ("108.61.103.46")
    port = 31810

# no testnet
