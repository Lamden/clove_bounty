from clove.network.bitcoin import Bitcoin


class Teacoin(Bitcoin):
    """
    Class with all the necessary Teacoin network information based on
    https://github.com/teacoind/teacoin/blob/master/src/chainparams.cpp
    (date of access: 02/21/2018)
    """
    name = 'teacoin'
    symbols = ('TEA', )
    seeds = ("66.85.164.76")
    port = 7921
	
# no testnet