from clove.network.bitcoin import Bitcoin


class Chesscoin(Bitcoin):
    """
    Class with all the necessary chesscoin network information based on
    https://github.com/coinforchess/chesscoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Chesscoin'
    symbols = ('CHESS', )
    seeds =  ("node.walletbuilders.com")
    port = 7323


# Has no Testnet