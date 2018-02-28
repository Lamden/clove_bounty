from clove.network.bitcoin import Bitcoin


class MonetaryUnit(Bitcoin):
    """
    Class with all the necessary MonetaryUnit network information based on
    https://github.com/muecoin/MUECore/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'monetaryunit'
    symbols = ('MUE', )
    seeds = ("nodes.muex.io",
             "nodes.monetaryunit.org",
             "nodes.mymue.com",
             "nodes.cryptophi.com")
    port = 19683


class MonetaryUnitTestNet(MonetaryUnit):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/muecoin/MUECore/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-monetaryunit'
    seeds = ("tnodes.muex.io")
    port = 18683
