from clove.network.bitcoin import Bitcoin


class Energycoin(Bitcoin):
    """
    Class with all the necessary Energycoin network information based on
    https://github.com/EnergyCoin/energycoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'energycoin'
    symbols = ('ENRG', )
    seeds = ("207.12.89.180",
             "212.114.59.109",
             "162.243.248.229")
    port = 22706
	
   
