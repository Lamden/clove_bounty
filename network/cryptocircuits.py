from clove.network.bitcoin import Bitcoin


class CryptoCircuits(Bitcoin):
    """
    Class with all the necessary CryptoCircuits network information based on
    https://github.com/circuitcoinproject/circuitcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptocircuits'
    symbols = ('CIRC', )
    seeds =  ("104.255.69.134")
    port = 17361
	
# Has no testnet