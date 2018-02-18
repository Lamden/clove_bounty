from clove.network.bitcoin import Bitcoin


class BeaverCoin(Bitcoin):
    """
    Class with all the necessary BeaverCoin network information based on
    https://github.com/BeaverCoin-Project/beavercoin/blob/master-0.10/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'beavervoin'
    symbols = ('BVC', )
    seeds =  ("dnsseed.beavercoin.org")
    port = 2333
	
   
class BeaverCoinTestNet(BeaverCoin):
    """
    Class with all the necessary BeaverCoin testing network information based on
    https://github.com/BeaverCoin-Project/beavercoin/blob/master-0.10/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-beavervoin'
    seeds = ("testnet-seed.beavercoin.org")
    port = 12333              