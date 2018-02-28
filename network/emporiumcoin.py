from clove.network.bitcoin import Bitcoin


class EmporiumCoin(Bitcoin):
    """
    Class with all the necessary EmporiumCoin network information based on
    https://github.com/emporiumcoin/EmporiumCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'emporiumcoin'
    symbols = ('EMPC', )
    seeds = ("40.68.31.20")
    port = 8295

# no testnet
