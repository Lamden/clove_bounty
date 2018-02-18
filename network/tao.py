from clove.network.bitcoin import Bitcoin


class Tao(Bitcoin):
    """
    Class with all the necessary Tao (XTO) network information based on
    https://github.com/taoblockchain/tao-core/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'tao'
    symbols = ('XTO', )
    seeds = ('taoexplorer.com', 'seed1.tao.network', 'seed2.tao.network' , 'seed3.tao.network',
			 'seed4.tao.network', 'seed5.tao.network', 'seed6.tao.network')
    port = 15150


class TaoTestNet(Tao):
    """
    Class with all the necessary Tao (XTO) testing network information based on
    https://github.com/taoblockchain/tao-core/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-tao'
    seeds = ('testnet.tao.network')
    port = 16160
