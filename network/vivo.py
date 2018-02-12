
from clove.network.bitcoin import Bitcoin


class Vivo(Bitcoin):
    """
    Class with all the necessary VIVO network information based on
    http://www.github.com/vivocoin/vivo/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'vivo'
    symbols = ('VIVO', )
    seeds = ('vivoseed1.vivoseeds.win',)
    port = 12845


class VivoTestNet(Vivo):
    """
    Class with all the necessary VIVO testing network information based on
    http://www.github.com/vivocoin/vivo/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-vivo'
    seeds = ('testnet-dns.vivonodes.space',)
    port = 13845
