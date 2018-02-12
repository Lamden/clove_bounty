from clove.network.bitcoin import Bitcoin


class Vertcoin(Bitcoin):
    """
    Class with all the necessary VTC network information based on
    https://github.com/vertcoin-project/vertcoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'vertcoin'
    symbols = ('VTC', )
    seeds = (
        'useast1.vtconline.org',
        'vtc.gertjaap.org',
        'seed.vtc.bryangoodson.org',
        'dnsseed.pknight.ca',
        'seed.orderofthetaco.org',
        'seed.alexturek.org',
        'vertcoin.mbl.cash'
    )
    port = 5889


class VertcoinTestNet(Vertcoin):
    """
    Class with all the necessary VTC testing network information based on
    https://github.com/vertcoin-project/vertcoin-core/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-vertcoin'
    seeds = (
        'jlovejoy.mit.edu',
        'gertjaap.ddns.net',
        'fr1.vtconline.org',
        'tvtc.vertcoin.org',
    )
    port = 15889
