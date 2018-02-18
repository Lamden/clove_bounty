from clove.network.bitcoin import Bitcoin


class Execoin(Bitcoin):
    """
    Class with all the necessary Execoin network information based on
    https://github.com/execoin/execoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'execoin'
    symbols = ('DMD', )
    seeds =  ("dnsseed.execoin.net")
    port = 9989
	
   
class ExecoinTestNet(Execoin):
    """
    Class with all the necessary Execoin testing network information based on
    https://github.com/execoin/execoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-execoin'
    seeds = ("testnet-seed.execoin.net")
    port = 19989              