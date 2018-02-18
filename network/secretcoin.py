from clove.network.bitcoin import Bitcoin


class SecretCoin(Bitcoin):
    """
    Class with all the necessary SecretCoin network information based on
    https://github.com/TeamSecret/SecretCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'secretcoin'
    symbols = ('SCRT', )
    seeds = ("23.227.190.110")
    port = 23152
	
# no testnet