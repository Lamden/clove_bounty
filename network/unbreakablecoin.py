from clove.network.bitcoin import Bitcoin


class UnbreakableCoin(Bitcoin):
    """
    Class with all the necessary UnbreakableCoin (UNB) network information based on
    https://github.com/jimblasko/UnbreakableCoin_2017/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'unbreakablecoin'
    symbols = ('UNB', )
    seeds = ('seed.ispace.co.uk', 'seed.multipool.us', '198.24.142.136')
    port = 9336

# no testnet
