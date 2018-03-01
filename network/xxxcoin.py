from clove.network.bitcoin import Bitcoin


class XxXcoin(Bitcoin):
    """
    Class with all the necessary XxXcoin network information based on
    https://github.com/devxxxcoin/xxxcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'xxxcoin'
    symbols = ('XXX', )
    seeds = ("85.214.147.99")
    port = 20133

# no testnet
