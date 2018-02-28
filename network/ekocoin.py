from clove.network.bitcoin import Bitcoin


class EcoCoin(Bitcoin):
    """
    Class with all the necessary ECO network information based on
    https://github.com/ekocoin/eko/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'ecocoin'
    symbols = ('ECO', )
    seeds = ("node.walletbuilders.com")
    port = 7257

# no testnet
