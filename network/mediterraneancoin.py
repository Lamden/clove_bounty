from clove.network.bitcoin import Bitcoin


class MediterraneanCoin(Bitcoin):
    """
    Class with all the necessary MediterraneanCoin network information based on
    https://github.com/mrtexaznl/mediterraneancoin/blob/exp-0.8.7.1/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mediterraneancoin'
    symbols = ('MED', )
    seeds = ("dnsseed.mediterraneancoin.org")
    port = 9373
	
   
class MediterraneanCoinTestNet(MediterraneanCoin):
    """
    Class with all the necessary MediterraneanCoin testing network information based on
    https://github.com/mrtexaznl/mediterraneancoin/blob/exp-0.8.7.1/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-mediterraneancoin'
    seeds = ("testnet-seed.mediterraneancoin.org")
    port = 19373              