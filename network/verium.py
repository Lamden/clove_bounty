from clove.network.bitcoin import Bitcoin


class Verium(Bitcoin):
    """
    Class with all the necessary Verium (VRM) network information based on
    https://github.com/VeriumReserve/verium/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'verium'
    symbols = ('VRM', )
    seeds = ('vrmdns.vericoin.info')
    port = 36988

# no testnet
