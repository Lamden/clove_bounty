from clove.network.bitcoin import Bitcoin


class Mooncoin(Bitcoin):
    """
    Class with all the necessary Mooncoin (MOON) network information based on
    https://github.com/mooncoincore/wallet/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'mooncoin'
    symbols = ('MOON', )
    seeds = ('node0.bazco.in', 'node1.bazco.in')
    port = 44664

# no testnet
