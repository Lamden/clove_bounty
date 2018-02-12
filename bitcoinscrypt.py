from clove.network.bitcoin import Bitcoin


class BitcoinScrypt(Bitcoin):
    """
    Class with all the necessary BitcoinScrypt network information based on
    https://github.com/bitcoin-scrypt/bitcoin-scrypt/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'BitcoinScrypt'
    symbols = ('BTCS', )
    seeds = ('altcoinwarz.com', '104.131.186.185')
    port = 30201


class BitcoinScryptTestNet(BitcoinScrypt):
    """
    Class with all the necessary BitcoinScrypt testing network information based on
    https://github.com/bitcoin-scrypt/bitcoin-scrypt/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-BitcoinScrypt'
    seeds = ()
    port = 30300  
	
	
	