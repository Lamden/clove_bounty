from clove.network.bitcoin import Bitcoin


class Gpucoin(Bitcoin):
    """
    Class with all the necessary GPU Coin (GPU) network information based on
    https://github.com/white92d15b7/gpu-coin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'gpucoin'
    symbols = ('GPU', )
    seeds = ('node1.gpucoin.market', 'node2.gpucoin.market', 'node3.gpucoin.market')
    port = 6897


class GpucoinTestNet(Gpucoin):
    """
    Class with all the necessary GPU Coin (GPU) testing network information based on
    https://github.com/white92d15b7/gpu-coin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-gpucoin'
    seeds = ()
    port = 16897
