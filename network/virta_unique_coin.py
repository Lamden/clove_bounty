from clove.network.bitcoin import Bitcoin


class VirtaUniqueCoin(Bitcoin):
    """
    Class with all the necessary Virta Unique Coin (VUC) network information based on
    https://github.com/virtauniquecoin/virtauniquecoin-master/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'virta-unique-coin'
    symbols = ('VUC', )
    seeds = ('50.63.163.129', )
    port = 15702


class VirtaUniqueCoinTestNet(VirtaUniqueCoin):
    """
    Class with all the necessary Virta Unique Coin (VUC) testing network information based on
    https://github.com/virtauniquecoin/virtauniquecoin-master/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-virta-unique-coin'
    seeds = ()
    port = 15703
