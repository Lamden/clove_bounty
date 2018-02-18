from clove.network.bitcoin import Bitcoin


class Virtacoin(Bitcoin):
    """
    Class with all the necessary Virtacoin (VTA) network information based on
    https://github.com/virtacoin/VirtaCoinProject/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'virtacoin'
    symbols = ('VTA', )
    seeds = ('seed1.virtacoin.com', 'seed2.virtacoin.com')
    port = 22816

# no testnet
