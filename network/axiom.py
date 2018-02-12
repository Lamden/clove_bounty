
from clove.network.bitcoin import Bitcoin


class Axiom(Bitcoin):
    """
    Class with all the necessary AXIOM network information based on
    http://www.github.com/axiomcryptocurrency/axiom/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'axiom'
    symbols = ('AXIOM', )
    seeds = ('seed.axiomcoin.xyz',)
    port = 15760


class AxiomTestNet(Axiom):
    """
    Class with all the necessary AXIOM testing network information based on
    http://www.github.com/axiomcryptocurrency/axiom/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-axiom'
    seeds = ()
    port = 25760
