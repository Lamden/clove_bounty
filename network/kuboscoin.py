from clove.network.bitcoin import Bitcoin


class KubosCoin(Bitcoin):
    """
    Class with all the necessary KubosCoin network information based on
    https://github.com/KUBOSCOIN/kubos/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kuboscoin'
    symbols = ('KUBO', )
    seeds = ("node.walletbuilders.com")
    port = 7715
