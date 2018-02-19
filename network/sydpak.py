from clove.network.bitcoin import Bitcoin


class SydPak(Bitcoin):
    """
    Class with all the necessary SydPak network information based on
    https://github.com/stewpak/Sydpak/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'sydpak'
    symbols = ('SDP', )
    seeds = ("89.204.139.80")
    port = 54321
	
# no testnet