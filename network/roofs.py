from clove.network.bitcoin import Bitcoin


class Roofs(Bitcoin):
    """
    Class with all the necessary  Roofs (ROOFS) network information based on
    https://github.com/roofsdev/roofs/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'roofs'
    symbols = ('ROOFS', )
    seeds = ('192.161.48.19')
    port = 20019


# no testnet
