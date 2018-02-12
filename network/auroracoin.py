from clove.network.bitcoin import Bitcoin


class AuroraCoin(Bitcoin):
    """
    Class with all the necessary AUR network information based on
    https://github.com/aurarad/auroracoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'auroracoin'
    symbols = ('AUR', )
    seeds = ('s1.auroraseed.net', 'aurseed1.criptoe.com', 's1.auroraseed.com', 's1.auroraseed.org', 's1.auroraseed.eu', 'electrum2.aurorcoin.is', 'electrum3.aurorcoin.is', 'electrum4.aurorcoin.is')
    port = 12340


class AuroraCoinTestNet(AuroraCoin):
    """
    Class with all the necessary AUR testing network information based on
    https://github.com/aurarad/auroracoin/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-auroracoin'
    seeds = ()
    port = None