from clove.network.bitcoin import Bitcoin


class Jiyo(Bitcoin):
    """
    Class with all the necessary Jiyo (JIYO) network information based on
    https://github.com/jiyocoin/jiyo-core/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'jiyo'
    symbols = ('JIYO', )
    seeds = ('node.jiyo.io', 'node2.jiyo.io')
    port = 22567

# no testnet
