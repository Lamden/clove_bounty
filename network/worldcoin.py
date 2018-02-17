from clove.network.bitcoin import Bitcoin


class Worldcoin(Bitcoin):
    """
    Class with all the necessary Worldcoin (WDC) network information based on
    https://github.com/worldcoinproject/worldcoin-v0.8/blob/master-0.8/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'worldcoin'
    symbols = ('WDC', )
    seeds = ('seednode1.worldcoincore.com', 'seednode2.worldcoincore.com', 'seednode3.worldcoincore.com',
			 'seednode4.worldcoincore.com', 'seednode5.worldcoincore.com', 'seednode6.worldcoincore.com')
    port = 11081


class WorldcoinTestNet(Worldcoin):
    """
    Class with all the necessary Worldcoin (WDC) testing network information based on
    https://github.com/worldcoinproject/worldcoin-v0.8/blob/master-0.8/src/net.cpp    
    (date of access: 02/16/2018)
    """
    name = 'test-worldcoin'
    seeds = ('testnet-seednode.worldcoincore.com')
    port = 21081
