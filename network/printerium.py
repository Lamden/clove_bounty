from clove.network.bitcoin import Bitcoin


class Printerium(Bitcoin):
    """
    Class with all the necessary Printerium network information based on
    https://github.com/printerium/printerium-project/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'printerium'
    symbols = ('PRX', )
    seeds = ("199.127.227.51")
    port = 10321


# Has no testnet
