from clove.network.bitcoin import Bitcoin


class Copperlark(Bitcoin):
    """
    Class with all the necessary Copperlark network information based on
    https://github.com/copperlark/clr/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'copperlark'
    symbols = ('CLR', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "dnsseed.bitcoin.dashjr.org",
             "bitseed.xf2.org")
    port = 10333
	
   
class CopperlarkTestNet(Copperlark):
    """
    Class with all the necessary Copperlark testing network information based on
    https://github.com/copperlark/clr/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-copperlark'
    seeds = ("testnet-seed.bitcoin.petertodd.org")
    port = 20333               