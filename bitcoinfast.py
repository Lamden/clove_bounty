from clove.network.bitcoin import Bitcoin


class BitcoinFast(Bitcoin):
    """
    Class with all the necessary Evilcoin network information based on
    https://github.com/crypto-currency/bitcoinfast/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'bitcoinfast'
    symbols = ('BCF', )
    seeds =  ("bitcoinfast.co")
    port = 25671

class BitcoinFastTestNet(BitcoinFast):
    """
    Class with all the necessary Evilcoin testing network information based on
    https://github.com/crypto-currency/bitcoinfast/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-bitcoinfast'
    seeds = ()
    port = 35671        
	
	
	