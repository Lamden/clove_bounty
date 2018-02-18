from clove.network.bitcoin import Bitcoin


class Moin(Bitcoin):
    """
    Class with all the necessary Moin (MOIN) network information based on
    https://github.com/MOIN/moin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'moin'
    symbols = ('MOIN', )
    seeds = ('seed.discovermoin.com', 'seed2.discovermoin.com')
    port = 7997


class MoinTestNet(Moin):
    """
    Class with all the necessary Moin (MOIN) testing network information based on
    https://github.com/MOIN/moin/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-moin'
    seeds = ('testnet-seed.discovermoin.com')
    port = 17997
