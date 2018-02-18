from clove.network.bitcoin import Bitcoin


class BiblePay(Bitcoin):
    """
    Class with all the necessary BiblePay (BBP) network information based on
    https://github.com/biblepay/biblepay/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'biblepay'
    symbols = ('BBP', )
    seeds =  ('dnsseed.biblepay.org', 'node.biblepay.org', 'dnsseed.biblepay-explorer.org')
    port = 40000


class BiblePayTestNet(BiblePay):
    """
    Class with all the necessary BiblePay (BBP) network information based on
    https://github.com/biblepay/biblepay/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-biblepay'
    symbols = ('BBP', )
    seeds =  ('testnet-seed.biblepaydot.io', 'test.dnsseed.masternode.io')
    port = 40001
