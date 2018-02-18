from clove.network.bitcoin import Bitcoin


class Grimcoin(Bitcoin):
    """
    Class with all the necessary Grimcoin (GRIM) network information based on
    https://github.com/GrimReaperCoins/GRIM/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'grimcoin'
    symbols = ('GRIM', )
    seeds = ('reaper.rocks', 'thec0de.com')
    port = 24861

# no testnet
