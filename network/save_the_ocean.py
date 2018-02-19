from clove.network.bitcoin import Bitcoin


class Save_The_Ocean(Bitcoin):
    """
    Class with all the necessary Save The Ocean network information based on
    https://github.com/SaveTheOceanMovement/SaveTheOceanCoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'save_the_ocean'
    symbols = ('STO', )
    seeds = ("52.169.14.55")
    port = 4555
	
# no testnet