from clove.network.bitcoin import Bitcoin


class CBit(Bitcoin):
    """
    Class with all the necessary C-Bit network information based on
    https://github.com/infernoman/c-bit/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'c-bit'
    symbols = ('XCT', )
    seeds = ("192.241.191.47","159.203.31.151")
    port = 18999


class CBitTestNet(CBit):
    """
    Class with all the necessary Photon testing network information based on
    https://github.com/infernoman/c-bit/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-c-bit'
    seeds = ("192.241.179.42")
    port = 18289 
	

	 