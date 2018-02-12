from clove.network.bitcoin import Bitcoin


class DBGold(Bitcoin):
    """
    Class with all the necessary DBG network information based on
    https://github.com/dbgold/dbgold/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'dbgold'
    symbols = ('DBG', )
    seeds = (
        '178.62.122.246',
    )
    port = 32113


class DBGoldTestNet(DBGold):
    """
    Class with all the necessary DBG testing network information based on
    https://github.com/dbgold/dbgold/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'test-dbgold'
    seeds = ()
    port = 44443
