from clove.network.bitcoin import Bitcoin


class PoisonIvyCoin(Bitcoin):
    """
    Class with all the necessary PoisonIvyCoin network information based on
    https://github.com/ivycoindev/ivy/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'poisonivycoin'
    symbols = ('XPS', )
    seeds = ("node.walletbuilders.com")
    port = 17783

# no testnet
