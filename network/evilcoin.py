from clove.network.bitcoin import Bitcoin


class Evilcoin(Bitcoin):
    """
    Class with all the necessary Evilcoin network information based on
    https://github.com/coins4lunch/evilcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'evilcoin'
    symbols = ('EVIL', )
    seeds = ("104.236.89.11", "192.241.198.44",
             "104.236.60.15", "45.55.157.54", "185.61.151.109")
    port = 20001

# Has no Testnet
