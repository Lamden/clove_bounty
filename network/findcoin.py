from clove.network.bitcoin import Bitcoin


class FindCoin(Bitcoin):
    """
    Class with all the necessary FindCoin network information based on
    https://github.com/SHNICI/Findcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'findcoin'
    symbols = ('FIND', )
    seeds = ("178.63.51.87")
    port = 55097

# no testnet
