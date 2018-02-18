from clove.network.bitcoin import Bitcoin


class Bitzeny(Bitcoin):
    """
    Class with all the necessary Bitzeny network information based on
    https://github.com/bitzeny/bitzeny/blob/z1.1.x/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitzeny'
    symbols = ('ZNY', )
    seeds =  ("seed.bitzeny.org")
    port = 9253
	
   
class BitzenyTestNet(Bitzeny):
    """
    Class with all the necessary Bitzeny testing network information based on
    https://github.com/bitzeny/bitzeny/blob/z1.1.x/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-bitzeny'
    seeds = ("testnet-seed.bitcoin.petertodd.org",
             "testnet-seed.bluematt.me")
    port = 19253              
	

