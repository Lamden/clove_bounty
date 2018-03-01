
from clove.network.bitcoin import Bitcoin


class MinexCoin(Bitcoin):
    """
    Class with all the necessary MNX network information based on
    http://www.github.com/minexcoin/minexcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'minexcoin'
    symbols = ('MNX', )
    seeds = ('138.197.73.48', '138.197.73.123', '159.203.70.193',
             '88.198.33.35', '95.85.35.152', '78.46.93.126', '91.233.111.28')
    port = 8335


class MinexCoinTestNet(MinexCoin):
    """
    Class with all the necessary MNX testing network information based on
    http://www.github.com/minexcoin/minexcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-minexcoin'
    seeds = (
        'seed.bitcoin.sipa.be', 'dnsseed.bluematt.me', 'dnsseed.bitcoin.dashjr.org', 'seed.bitcoinstats.com',
        'seed.bitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch', 'seed.tbtc.petertodd.org',
        'testnet-seed.bluematt.me', 'testnet-seed.bitcoin.schildbach.de'
    )
    port = 18333
