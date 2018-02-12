
from clove.network.bitcoin import Bitcoin


class Bitvolt(Bitcoin):
    """
    Class with all the necessary VOLT network information based on
    http://www.github.com/voltcoin/Volt/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bitvolt'
    symbols = ('VOLT', )
    seeds = ('198.211.126.38',)
    port = 11516


class BitvoltTestNet(Bitvolt):
    """
    Class with all the necessary VOLT testing network information based on
    http://www.github.com/voltcoin/Volt/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bitvolt'
    seeds = ()
    port = 25723
