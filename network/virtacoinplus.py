from clove.network.bitcoin import Bitcoin


class VirtacoinPlus(Bitcoin):
    """
    Class with all the necessary VirtacoinPlus (XVP) network information based on
    https://github.com/virtacoinplus/virtacoinplus/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'virtacoinplus'
    symbols = ('XVP', )
    seeds = ('93.183.225.204', '159.203.67.177', '81.169.212.185', '45.55.89.137',
             '188.166.168.122', '128.199.41.227', '138.197.101.132', '138.68.242.151')
    port = 6032

# no testnet
