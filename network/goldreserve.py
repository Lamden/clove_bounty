from clove.network.bitcoin import Bitcoin


class GoldReserve(Bitcoin):
    """
    Class with all the necessary GoldReserve network information based on
    https://github.com/mesterlovesz74/goldreserve/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'goldreserve'
    symbols = ('XGR', )
    seeds = ('108.61.103.33', '5.250.177.24')
    port = 21192
