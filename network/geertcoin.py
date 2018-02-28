from clove.network.bitcoin import Bitcoin


class GeertCoin(Bitcoin):
    """
    Class with all the necessary GeertCoin network information based on
    https://github.com/geertaltcoin/geertcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'geertcoin'
    symbols = ('GEERT', )
    seeds = ('dnsseed.geertcoin.com')
    port = 64333


# Has no Testnet
