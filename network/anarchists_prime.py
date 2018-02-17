from clove.network.bitcoin import Bitcoin


class  AnarchistsPrime(Bitcoin):
    """
    Class with all the necessary  AnarchistsPrime (ACP) network information based on
    https://github.com/AmmoCore/AmmoReloaded/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'anarchistsprime'
    symbols = ('ACP', )
    seeds =  ('acp.servep2p.com', '159.203.31.42', '139.59.255.88', '138.68.143.185', '138.68.14.183', '188.166.175.90', '203.212.152.229')
    port = 11050


class  AnarchistsPrimeTestNet(Aces):
    """
    Class with all the necessary  AnarchistsPrime (ACP) network information based on
    https://github.com/AmmoCore/AmmoReloaded/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-anarchistsprime'
    symbols = ('ACP', )
    seeds =  ()
    port = 5744