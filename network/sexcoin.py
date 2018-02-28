
from clove.network.bitcoin import Bitcoin


class Sexcoin(Bitcoin):
    """
    Class with all the necessary SXC network information based on
    http://www.github.com/sexcoin-project/sexcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'sexcoin'
    symbols = ('SXC', )
    seeds = ('dnsseed.sexcoin.info', 'dnsseed.lavajumper.com')
    port = 9560


class SexcoinTestNet(Sexcoin):
    """
    Class with all the necessary SXC testing network information based on
    http://www.github.com/sexcoin-project/sexcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-sexcoin'
    seeds = ('dnsseed.litecoinpool.org', 'testnet-seed.sexcoin.info',
             'testnet-seed.ltc.xurious.com', 'dnsseed.wemine-testnet.com')
    port = 19560
