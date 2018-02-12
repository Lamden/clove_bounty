from clove.network.bitcoin import Bitcoin


class LUXCoin(Bitcoin):
    """
    Class with all the necessary LUX network information based on
    https://github.com/216k155/lux/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'luxcoin'
    symbols = ('LUX', )
    seeds = ('5.189.142.181', '5.77.44.147', '209.250.254.156', '45.76.114.209', 'luxseed1.luxcore.io', 'luxseed2.luxcore.io', 'luxseed3.luxcore.io', 'luxseed4.luxcore.io')
    port = 26868


class LUXCoinTestNet(ZCoin):
    """
    Class with all the necessary LUX testing network information based on
    https://github.com/216k155/lux/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-luxcoin'
    seeds = ('88.198.192.110')
    port = 28333
	
    