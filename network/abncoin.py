from clove.network.bitcoin import Bitcoin


class Abncoin(Bitcoin):
    """
    Class with all the necessary Abncoin network information based on
    https://github.com/AbnMainDev/abncoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'abncoin'
    symbols = ('ABN', )
    seeds = ("node.walletbuilders.com")
    port = 10267
	
# no testnet