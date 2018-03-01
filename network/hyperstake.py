from clove.network.bitcoin import Bitcoin


class HyperStake(Bitcoin):
    """
    Class with all the necessary HyperStake network information based on
   https://github.com/hyperstake/hyperstake/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'hyperstake'
    symbols = ('HYP', )
    seeds = ('hyp.seed.fuzzbawls.pw', 'hypseed.presstab.pw')
    port = 18775


# Has no Testnet
