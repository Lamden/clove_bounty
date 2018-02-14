from clove.network.bitcoin import Bitcoin


class CoolCoin(Bitcoin):
    """
    Class with all the necessary CoolCoin network information based on
    https://github.com/coollovecoin/coolcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'coolcoin'
    symbols = ('COOL', )
    seeds =  ("dnsseed2.coolcoin.info)
    port = 13581
	
# Has no testnet