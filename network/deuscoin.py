from clove.network.bitcoin import Bitcoin


class DeusCoin(Bitcoin):
    """
    Class with all the necessary DeusCoin (DEUS) network information based on
    https://github.com/deuscoin-org/deuscoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'deuscoin'
    symbols = ('DEUS', )
    seeds = ('54.169.70.29')
    port = 19697

# no testnet
