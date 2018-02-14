from clove.network.bitcoin import Bitcoin


class CAIx(Bitcoin):
    """
    Class with all the necessary CAIx network information based on
    https://github.com/Lefter1s/CAIx/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'CAIx'
    symbols = ('CAIx', )
    seeds = ("82.196.2.163",
             "37.187.78.114",
             "walrusbonzo.ddns.net",
             "alpho2k.ddns.net")
    port = 1511
	
# Has no testnet

	