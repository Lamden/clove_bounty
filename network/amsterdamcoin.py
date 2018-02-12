
from clove.network.bitcoin import Bitcoin


class AmsterdamCoin(Bitcoin):
    """
    Class with all the necessary AMS network information based on
    http://www.github.com/CoinProjects/AmsterdamCoin-v4/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'amsterdamcoin'
    symbols = ('AMS', )
    seeds = ('nl-1.amsterdamcoin.com', 'us-1.amsterdamcoin.com', 'us-2.amsterdamcoin.com', 'eu-1.amsterdamcoin.com', 'eu-2.amsterdamcoin.com', 'asia-1.amsterdamcoin.com')
    port = 50020


class AmsterdamCoinTestNet(AmsterdamCoin):
    """
    Class with all the necessary AMS testing network information based on
    http://www.github.com/CoinProjects/AmsterdamCoin-v4/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-amsterdamcoin'
    seeds = ('amsterdamcoin-testnet.seed.fuzzbawls.pw', 'amsterdamcoin-testnet.seed2.fuzzbawls.pw', 's3v3nh4cks.ddns.net', '88.198.192.110')
    port = 51474
