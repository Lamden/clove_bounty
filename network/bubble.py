
from clove.network.bitcoin import Bitcoin


class Bubble(Bitcoin):
    """
    Class with all the necessary BUB network information based on
    http://www.github.com/spayse/Bubble/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'bubble'
    symbols = ('BUB', )
    seeds = ('194.135.85.45',)
    port = 15716


class BubbleTestNet(Bubble):
    """
    Class with all the necessary BUB testing network information based on
    http://www.github.com/spayse/Bubble/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-bubble'
    seeds = ()
    port = 38881
