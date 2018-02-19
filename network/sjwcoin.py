from clove.network.bitcoin import Bitcoin


class SJWCoin(Bitcoin):
    """
    Class with all the necessary SJWCoin network information based on
    https://github.com/sjwcoin/sjwcoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sjwcoin'
    symbols = ('SJW', )
    seeds = ("seed.sjwcoin.com")
    port = 19966
	
# no testnet