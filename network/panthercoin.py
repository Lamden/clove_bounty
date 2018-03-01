from clove.network.bitcoin import Bitcoin


class PantherCoin(Bitcoin):
    """
    Class with all the necessary PantherCoin network information based on
    https://github.com/panthercoin/Panther/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'panthercoin'
    symbols = ('PINKX', )
    seeds = ("node.walletbuilders.com", )
    port = 6641

# no testnet
