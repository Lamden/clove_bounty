from clove.network.bitcoin import Bitcoin


class SmartCoin(Bitcoin):
    """
    Class with all the necessary SmartCoin network information based on
    https://github.com/psionin/smartcoin/blob/0.11/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'smartcoin'
    symbols = ('SMC', )
    seeds = ("dnsseed.smartcoin.cc")
    port = 58585
	
   
class DiamondTestNet(SmartCoin):
    """
    Class with all the necessary SmartCoin testing network information based on
    https://github.com/psionin/smartcoin/blob/0.11/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-smartcoin'
    seeds = ("testnet-seed.alexykot.me",
            "testnet-seed.bitcoin.petertodd.org",
            "testnet-seed.bluematt.me",
            "testnet-seed.bitcoin.schildbach.de")
    port = 18333              
	
