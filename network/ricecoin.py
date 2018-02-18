from clove.network.bitcoin import Bitcoin


class RiceCoin(Bitcoin):
    """
    Class with all the necessary RiceCoin network information based on
    https://github.com/TeamRicecoin/Ricecoin-project/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ricecoin'
    symbols = ('RICE', )
    seeds = ("130.193.81.218")
    port = 41981
	
# no testnet