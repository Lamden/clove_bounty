from clove.network.bitcoin import Bitcoin


class ZetaMicron(Bitcoin):
    """
    Class with all the necessary ZetaMicron (ZMC) network information based on
    https://github.com/zmcdev/ZMcron/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'zetamicron'
    symbols = ('ZMC', )
    seeds = ('node.walletbuilders.com')
    port = 9077

# no testnet
