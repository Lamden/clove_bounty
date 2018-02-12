
from clove.network.bitcoin import Bitcoin


class MarxCoin(Bitcoin):
    """
    Class with all the necessary MARX network information based on
    http://www.github.com/MARXCOIN01/MARX/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'marxcoin'
    symbols = ('MARX', )
    seeds = ('seed4.cryptolife.net', 'seed2.cryptolife.net', 'seed3.cryptolife.net', 'electrum3.cryptolife.net')
    port = 41103


class MarxCoinTestNet(MarxCoin):
    """
    Class with all the necessary MARX testing network information based on
    http://www.github.com/MARXCOIN01/MARX/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-marxcoin'
    seeds = ()
    port = 141103
