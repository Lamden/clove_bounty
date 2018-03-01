from clove.network.bitcoin import Bitcoin


class Magnet(Bitcoin):
    """
    Class with all the necessary Magnet network information based on
    https://github.com/magnetwork/magnet/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'magnet'
    symbols = ('MAG', )
    seeds = ("magdns1.magnetwork.io",
             "magdns2.magnetwork.io",
             "magdns3.magnetwork.io")
    port = 17177

# no test net
