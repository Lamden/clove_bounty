from clove.network.bitcoin import Bitcoin


class LevoPlus(Bitcoin):
    """
    Class with all the necessary LevoPlus (LVPS) network information based on
    https://github.com/levoplus/Levoplus-Cryptocurrency-Source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'levoplus'
    symbols = ('LVPS', )
    seeds = ('104.131.114.154', '45.55.63.49', 'electrum4.cryptolife.net')
    port = 25593

# no testnet
