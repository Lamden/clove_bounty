from clove.network.bitcoin import Bitcoin


class Allion(Bitcoin):
    """
    Class with all the necessary Allion network information based on
    https://github.com/epyxz/allion/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'allion'
    symbols = ('ALL', )
    seeds = 	("node1.trollpay.com",
                 "node2.trollpay.com",
                 "node3.trollpay.com",
                 "node4.trollpay.com",
                 "node1.allion.xyz",
                 "node2.allion.xyz",
                 "node3.allion.xyz",
                 "node4.allion.xyz",
                 "node5.allion.xyz",
                 "node6.allion.xyz",
                 "node7.allion.xyz",
                 "node8.allion.xyz",
                 "node9.allion.xyz",
                 "node10.allion.xyz")
    port = 12916



# No Testnet