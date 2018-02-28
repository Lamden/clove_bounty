from clove.network.bitcoin import Bitcoin


class Blackstar(Bitcoin):
    """
    Class with all the necessary BSTAR network information based on
    https://github.com/bstarcoin/blackstar/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'blackstar'
    symbols = ('BSTAR', )
    seeds = ()
    port = 16878


class BlackstarTestNet(Blackstar):
    """
    Class with all the necessary BSTAR testing network information based on
    https://github.com/bstarcoin/blackstar/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-blackstar'
    seeds = ()
    port = 16879
