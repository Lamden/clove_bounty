from clove.network.bitcoin import Bitcoin


class ChoofCoin(Bitcoin):
    """
    Class with all the necessary ChoofCoin network information based on
    https://github.com/choofcoin/choofcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'choofcoin'
    symbols = ('CHOOF', )
    seeds = ("162.243.1.45")
    port = 7777

# Has no testnet
