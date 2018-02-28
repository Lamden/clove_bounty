from clove.network.bitcoin import Bitcoin


class ExitCoin(Bitcoin):
    """
    Class with all the necessary ExitCoin network information based on
    https://github.com/exitcoin/exit/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'exitcoin'
    symbols = ('EXIT', )
    seeds = ("node.walletbuilders.com")
    port = 7381

# no testnet
