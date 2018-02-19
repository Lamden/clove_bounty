from clove.network.bitcoin import Bitcoin


class TrollTokens(Bitcoin):
    """
    Class with all the necessary trolltokens network information based on
    https://github.com/Justbob1956/TrollTokens/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'trolltokens'
    symbols = ('TKN', )
    seeds = ("68.117.4.111")
    port = 16385
	
# no testnet