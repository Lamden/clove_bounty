from clove.network.bitcoin import Bitcoin


class Creditbit(Bitcoin):
    """
    Class with all the necessary Creditbit network information based on
    https://github.com/creditbit/creditbit/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'creditbit'
    symbols = ('CRBIT', )
    seeds = ("dnsseed.creditbit.org",
             "node1.creditbit.org",
             "node2.creditbit.org",
             "node3.creditbit.org",
             "node4.creditbit.org",
             "node5.creditbit.org",
             "node6.creditbit.org",
             "node7.creditbit.org",
             "node8.creditbit.org",
             "node9.creditbit.org",
             "node10.creditbit.org")	
    port = 5556
	
# Has no testnet