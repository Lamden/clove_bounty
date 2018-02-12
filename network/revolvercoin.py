
from clove.network.bitcoin import Bitcoin


class RevolverCoin(Bitcoin):
    """
    Class with all the necessary XRE network information based on
    https://github.com/revolvercoin/revolvercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'revolvercoin'
    symbols = ('XRE', )
    seeds = ()
    port = 8777


class RevolverCoinTestNet(RevolverCoin):
    """
    Class with all the necessary XRE testing network information based on
    https://github.com/revolvercoin/revolvercoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-revolvercoin'
    seeds = ()
    port = 18777