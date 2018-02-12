
from clove.network.bitcoin import Bitcoin


class Joulecoin(Bitcoin):
    """
    Class with all the necessary XJO network information based on
    http://www.github.com/joulecoin/joulecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'joulecoin'
    symbols = ('XJO', )
    seeds = ('seed1.jouleco.in', 'seed2.jouleco.in', 'seed3.jouleco.in', 'seed4.jouleco.in', 'joulecoin1.chickenkiller.com', 'joulecoin2.crabdance.com')
    port = 26789


class JoulecoinTestNet(Joulecoin):
    """
    Class with all the necessary XJO testing network information based on
    http://www.github.com/joulecoin/joulecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-joulecoin'
    seeds = ('testseed1.jouleco.in',)
    port = 26783
