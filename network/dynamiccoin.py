from clove.network.bitcoin import Bitcoin


class DynamicCoin(Bitcoin):
    """
    Class with all the necessary DynamicCoin (DMC) network information based on
    https://github.com/DynamicCoinOrg/DMC/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'dynamiccoin'
    symbols = ('DMC', )
    seeds = ('main.seeds.dynamiccoin.net')
    port = 7333


class DynamicCoinTestNet(DynamicCoin):
    """
    Class with all the necessary DynamicCoin (DMC) testing network information based on
    https://github.com/DynamicCoinOrg/DMC/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-dynamiccoin'
    seeds = ('test.seeds.dynamiccoin.net')
    port = 17333
