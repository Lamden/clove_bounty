from clove.network.bitcoin import Bitcoin


class Virtauniquecoin(Bitcoin):
    """
    Class with all the necessary Virta Unique Coin (VUC) network information based on
    https://github.com/virtauniquecoin/virtauniquecoin-master/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'virtauniquecoin'
    symbols = ('VUC', )
    seeds = ('50.63.163.129')
    port = 15702


class VirtauniquecoinTestNet(Virtauniquecoin):
    """
    Class with all the necessary Virta Unique Coin (VUC) testing network information based on
    https://github.com/virtauniquecoin/virtauniquecoin-master/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-virtauniquecoin'
    seeds = ()
    port = 15703
