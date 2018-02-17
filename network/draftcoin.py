from clove.network.bitcoin import Bitcoin


class DraftCoin(Bitcoin):
    """
    Class with all the necessary DraftCoin network information based on
    https://github.com/btcdraft/draftcoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'draftcoin'
    symbols = ('DFT', )
    seeds = ("node1.btcdraft.com",
             "node2.btcdraft.com",
             "node3.btcdraft.com",
             "node4.btcdraft.com",
             "node5.btcdraft.com",
             "node6.btcdraft.com",
             "node7.btcdraft.com",
             "node8.btcdraft.com",
             "node9.btcdraft.com",
             "node10.btcdraft.com",
             "node11.btcdraft.com",
             "node12.btcdraft.com",
             "node13.btcdraft.com",
             "node14.btcdraft.com",
             "node15.btcdraft.com",
             "node16.btcdraft.com",
             "node17.btcdraft.com",
             "node18.btcdraft.com",
             "node19.btcdraft.com",
             "node20.btcdraft.com",
             "node21.btcdraft.com",
             "node22.btcdraft.com",
             "node23.btcdraft.com",
             "node24.btcdraft.com",
             "node25.btcdraft.com",
             "dns.btcdraft.ca",
             "204.188.161.57",
             "149.56.101.219",
             "158.69.199.130",
             "204.188.161.61",
             "99.248.230.242",
             "68.206.29.192",
             "209.195.104.6")
    port = 20302
	
# no testnet