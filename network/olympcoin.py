from clove.network.bitcoin import Bitcoin


class OlympCoin(Bitcoin):
    """
    Class with all the necessary OlympCoin network information based on
    https://github.com/olympcoin/OlympCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'olympcoin'
    symbols = ('OLYMP', )
    seeds = ("40.68.155.213")
    port = 3530

# no testnet
