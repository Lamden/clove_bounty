from clove.network.bitcoin import Bitcoin


class ShadowCash(Bitcoin):
    """
    Class with all the necessary ShadowCash (SDC) network information based on
    https://github.com/shadowproject/shadow/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'shadowcash'
    symbols = ('SDC', )
    seeds = ('seed.shadow.cash', 'seed2.shadow.cash', 'seed3.shadow.cash', 'seed4.shadow.cash', 'seed.shadowproject.io', 'seed.shadowchain.info')
    port = 51737

# no testnet
