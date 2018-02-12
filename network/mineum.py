from clove.network.bitcoin import Bitcoin


class Mineum(Bitcoin):
    """
    Class with all the necessary Mineum network information based on
    https://github.com/antho281/mineum/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Mineum'
    symbols = ('MNM', )
    seeds = ('24.37.43.158:31316', '45.45.88.18:31319', 'nodes.muex.io')
    port = 31316


# Has no Testnet