from clove.network.bitcoin import Bitcoin


class Monero(Bitcoin):
    """
    Class with all the necessary Monero (XMR) network information based on
    https://github.com/monero-project/monero/blob/master/src/p2p/net_node.inl
    (date of access: 02/22/2018)
    """
    name = 'monero'
    symbols = ('XMR', )
    seeds = ('107.152.130.98',
			 '212.83.175.67',
			 '5.9.100.248',
			 '163.172.182.165',
			 '161.67.132.39',
			 '198.74.231.92')
    port = 18080


class MoneroTestNet(Monero):
    """
    Class with all the necessary Monero (XMR) testing network information based on
    https://github.com/monero-project/monero/blob/master/src/p2p/net_node.inl    
    (date of access: 02/22/2018)
    """
    name = 'test-monero'
    seeds = ('212.83.175.67',
			 '5.9.100.248',
			 '163.172.182.165',
			 '195.154.123.123',
			 '212.83.172.165')
    port = 28080
