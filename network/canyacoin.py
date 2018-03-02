from clove.network.bitcoin import Bitcoin


class CanYaCoin(Bitcoin):
    """
    Class with all the necessary CanYaCoin network information based on
    https://github.com/216k155/Canyacoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'canyacoin'
    symbols = ('CAN', )
    seeds = ("dnsseed.canya.io", )
    port = 9033


class CanYaCoinTestNet(CanYaCoin):
    """
    Class with all the necessary CanYaCoin testing network information based on
    https://github.com/216k155/Canyacoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-canyacoin'
    seeds = ("dnsseed.testnet.canya.io", )
    port = 19133
