from clove.network.bitcoin import Bitcoin


class Nyancoin(Bitcoin):
    """
    Class with all the necessary Nyancoin network information based on
    https://github.com/nyancoin-release/nyancoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'Nyancoin'
    symbols = ('NYAN', )
    seeds = ("nyanseed.com")
    port = 33701

# no testnet
