
from clove.network.bitcoin import Bitcoin


class ZCoin(Bitcoin):
    """
    Class with all the necessary XZC network information based on
    http://www.github.com/zcoinofficial/zcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'zcoin'
    symbols = ('XZC', )
    seeds = ('sf1.zcoin.io', 'sf2.zcoin.io', 'london.zcoin.io', 'singapore.zcoin.io', 'nyc.zcoin.io')
    port = 8168


class ZCoinTestNet(ZCoin):
    """
    Class with all the necessary XZC testing network information based on
    http://www.github.com/zcoinofficial/zcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-zcoin'
    seeds = ('beta1.zcoin.io', 'beta2.zcoin.io', 'testnet-seed.bitcoin.jonasschnelli.ch', 'seed.tbtc.petertodd.org', 'testnet-seed.bluematt.me', 'testnet-seed.bitcoin.schildbach.de')
    port = 18168
