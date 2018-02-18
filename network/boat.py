from clove.network.bitcoin import Bitcoin


class BOAT(Bitcoin):
    """
    Class with all the necessary BOAT network information based on
    https://github.com/OBAViJEST/boatcoinfinal/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'boat'
    symbols = ('BOAT', )
    seeds = ("seed1.Doubloon.trade",
             "seed2.Doubloon.trade",
             "seed3.Doubloon.trade",
             "seed4.Doubloon.trade")
    port = 33827
	
# Has no testnet