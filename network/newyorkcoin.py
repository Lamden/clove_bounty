from clove.network.bitcoin import Bitcoin


class NewYorkCoin(Bitcoin):
    """
    Class with all the necessary NewYorkCoin network information based on
    https://github.com/NewYorkCoin/newyorkc/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'newyorkcoin'
    symbols = ('NYC', )
    seeds = ("seed.ds.newyorkco.in","seed.newyorkco.in")	
    port = 17020

# no testnet