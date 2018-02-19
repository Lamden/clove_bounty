from clove.network.bitcoin import Bitcoin


class PRCoin(Bitcoin):
    """
    Class with all the necessary PRCoin network information based on
    https://github.com/prcoin/prcoin-wallet
    (date of access: 02/19/2018)
    """
    name = 'prcoin'
    symbols = ('PRC', )
    seeds = ("73.78.96.65:52698",
             "218.144.45.133:50090",
             "218.144.45.133:51045",
             "218.144.45.133:61276")
    port = 8535
	
# no testnet