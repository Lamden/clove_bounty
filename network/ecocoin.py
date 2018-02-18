from clove.network.bitcoin import Bitcoin


class EcoCoin(Bitcoin):
    """
    Class with all the necessary EcoCoin (ECO) network information based on
    https://github.com/ECOcoin-src/ECO-source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ecocoin'
    symbols = ('ECO', )
    seeds = ('ecocoin.info')
    port = 11047

# no testnet
