from clove.network.bitcoin import Bitcoin


class Antibitcoin(Bitcoin):
    """
    Class with all the necessary Antibitcoin network information based on
    https://github.com/antibitcoin/antibitcoin-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Antibitcoin'
    symbols ('ANTI', )
    seeds = ('188.213.171.167', '108.61.165.75')
    port = 11650


# Has no Testnet