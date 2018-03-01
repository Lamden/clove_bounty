
from clove.network.bitcoin import Bitcoin


class CrowdCoin(Bitcoin):
    """
    Class with all the necessary CRC network information based on
    http://www.github.com/crowdcoinChain/Crowdcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'crowdcoin'
    symbols = ('CRC', )
    seeds = ('crowdcoin1.masterhash.us', 'crowdcoin2.masterhash.us', 'crowdcoin3.masterhash.us',
             'crowdcoin4.masterhash.us', 'crowdcoin5.masterhash.us', 'crowdcoin6.masterhash.us')
    port = 12875


class CrowdCoinTestNet(CrowdCoin):
    """
    Class with all the necessary CRC testing network information based on
    http://www.github.com/crowdcoinChain/Crowdcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-crowdcoin'
    seeds = ('dns.shmest.win', 'testnet-dns.crowdcoinnodes.space')
    port = 13845
