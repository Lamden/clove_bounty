from clove.network.bitcoin import Bitcoin


class Syndicate(Bitcoin):
    """
    Class with all the necessary  Syndicate (SYNX) network information based on
    https://github.com/SyndicateLtd/SyndicateQT/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'syndicate'
    symbols = ('SYNX', )
    seeds = ('seed.synx.online')
    port = 9999


class SyndicateTestNet(Syndicate):
    """
    Class with all the necessary  Syndicate (SYNX) network information based on
    https://github.com/SyndicateLtd/SyndicateQT/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-syndicate'
    symbols = ('SYNX', )
    seeds = ('')
    port = 27170
