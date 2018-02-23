from clove.network.bitcoin import Bitcoin


class GalaxyCoin(Bitcoin):
    """
    Class with all the necessary GalaxyCoin network information based on
    https://github.com/m0gliE/galaxycoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'galaxycoin'
    symbols = ('GLX', )
    seeds = ("galaxycoin.no-ip.biz")
    port = 15521
	
# no testnet