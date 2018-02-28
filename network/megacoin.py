
from clove.network.bitcoin import Bitcoin


class Megacoin(Bitcoin):
    """
    Class with all the necessary MEC network information based on
    http://www.github.com/LIMXTEC/Megacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'megacoin'
    symbols = ('MEC', )
    seeds = ('185.194.142.125',)
    port = 7951


class MegacoinTestNet(Megacoin):
    """
    Class with all the necessary MEC testing network information based on
    http://www.github.com/LIMXTEC/Megacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-megacoin'
    seeds = ('185.194.140.60', 'dnsseed.megacoin.in', '144.76.118.88', '108.61.179.50',
             '108.61.179.50', 'testnet-seed.ltc.xurious.com', 'dnsseed.wemine-testnet.com')
    port = 17951
