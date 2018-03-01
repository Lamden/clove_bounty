from clove.network.bitcoin import Bitcoin


class GSMcoin(Bitcoin):
    """
    Class with all the necessary GSMcoin network information based on
    https://github.com/gsmcoin/GSMcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'gsmcoin'
    symbols = ('GSM', )
    seeds = ("195.34.100.2")
    port = 18446

# no testnet
