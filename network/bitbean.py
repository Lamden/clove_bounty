from clove.network.bitcoin import Bitcoin


class Photon(Bitcoin):
    """
    Class with all the necessary Photon network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'photon'
    symbols = ('PHO', )
    seeds = ("165.227.200.255")
    port = 35556


class PhotonTestNet(Photon):
    """
    Class with all the necessary Photon testing network information based on
    https://github.com/beatscoindev/beatscoinv2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-photon'
    seeds = ("photon.info")
    port = 18992 
	

	 