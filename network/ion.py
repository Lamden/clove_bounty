from clove.network.bitcoin import Bitcoin


class ION(Bitcoin):
    """
    Class with all the necessary ION (ION) network information based on
    https://github.com/ionomy/ion/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'ion'
    symbols = ('ION', )
    seeds = ('main.seeder.baseserv.com', 'main.seeder.uksafedns.net')
    port = 12700


class IONTestNet(ION):
    """
    Class with all the necessary ION (ION) testing network information based on
    https://github.com/ionomy/ion/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-ion'
    seeds = ('testnet.seeder.baseserv.com', 'testnet.seeder.uksafedns.net')
    port = 27170
