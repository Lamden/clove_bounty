from clove.network.bitcoin import Bitcoin


class TargetCoin(Bitcoin):
    """
    Class with all the necessary TargetCoin network information based on
    https://github.com/TargetCoin/TargetCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'targetcoin '
    symbols = ('TAR', )
    seeds = ("192.168.145.1")
    port = 56680
	
# no testnet