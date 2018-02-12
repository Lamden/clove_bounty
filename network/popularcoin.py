
from clove.network.bitcoin import Bitcoin


class PopularCoin(Bitcoin):
    """
    Class with all the necessary POP network information based on
    http://www.github.com/Pop-Currency-Foundation/PopularCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'popularcoin'
    symbols = ('POP', )
    seeds = ('209.239.122.186', '64.137.223.85', '64.137.230.215', '64.137.223.95', '64.137.226.19', '45.62.213.215', '45.62.250.59', '104.233.107.18', '45.62.244.166', '62.59.168.89', '163.172.86.142', '72.221.91.113', '51.254.45.117', '84.2.34.93', '66.229.179.157', '52.178.75.124', '85.236.188.28', '83.58.120.241', '167.88.15.89', '217.175.119.125', '188.134.72.213', '47.156.228.24', '108.170.1.134', '139.162.235.42')
    port = 9426


class PopularCoinTestNet(PopularCoin):
    """
    Class with all the necessary POP testing network information based on
    http://www.github.com/Pop-Currency-Foundation/PopularCoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-popularcoin'
    seeds = ('seedtest.popularcoin.info/node',)
    port = 19222
