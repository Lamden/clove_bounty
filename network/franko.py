
from clove.network.bitcoin import Bitcoin


class Franko(Bitcoin):
    """
    Class with all the necessary FRK network information based on
    http://www.github.com/franko-org/franko/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'franko'
    symbols = ('FRK', )
    seeds = ('seed.bitcoin.sipa.be',)
    port = 8333


class FrankoTestNet(Franko):
    """
    Class with all the necessary FRK testing network information based on
    http://www.github.com/franko-org/franko/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-franko'
    seeds = ('dnsseed.bluematt.me', 'dnsseed.bitcoin.dashjr.org', 'seed.bitcoinstats.com', 'bitseed.xf2.org', 'seed.bitcoin.jonasschnelli.ch', 'testnet-seed.alexykot.me', 'testnet-seed.bitcoin.petertodd.org', 'testnet-seed.bluematt.me', 'testnet-seed.bitcoin.schildbach.de')
    port = 18333
