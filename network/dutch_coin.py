from clove.network.bitcoin import Bitcoin


class DutchCoin(Bitcoin):
    """
    Class with all the necessary Dutch Coin (DUTCH) network information based on
    https://github.com/devdutch/dutch/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'dutchcoin'
    symbols = ('DUTCH', )
    seeds = ('198.136.28.100')
    port = 20717

# no testnet
