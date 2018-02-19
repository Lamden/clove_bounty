from clove.network.bitcoin import Bitcoin


class GEN(Bitcoin):
    """
    Class with all the necessary G3N (G3N) network information based on
    https://github.com/GenStakeTeam/genstake/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'g3n'
    symbols = ('G3N', )
    seeds = ('genseed.presstab.pw', 'gen.seed.fuzzbawls.pw', 'gen.netcraft.ch')
    port = 9341

# no testnet
