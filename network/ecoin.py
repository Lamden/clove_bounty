from clove.network.bitcoin import Bitcoin


class ECoin(Bitcoin):
    """
    Class with all the necessary  E-coin (ECN) network information based on
    https://github.com/ecoinclub/ecoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'ecoin'
    symbols = ('ECN', )
    seeds = ('138.68.164.92', 'ecnblockchain.com',
             '72.52.156.4', '72.52.156.87')
    port = 18741


# no testnet
