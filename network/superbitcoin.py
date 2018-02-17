from clove.network.bitcoin import Bitcoin


class  SuperBitcoin(Bitcoin):
    """
    Class with all the necessary  SuperBitcoin (SBTC) network information based on
    https://github.com/superbitcoin/SuperBitcoin/blob/master/src/config/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'superbitcoin'
    symbols = ('SBTC', )
    seeds =  ('seed.superbtca.com', 'seed.superbtca.info', 'seed.superbtc.org')
    port = 8334


class  SuperBitcoinTestNet(SuperBitcoin):
    """
    Class with all the necessary  SuperBitcoin (SBTC) network information based on
    https://github.com/superbitcoin/SuperBitcoin/blob/master/src/config/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-superbitcoin'
    symbols = ('SBTC', )
    seeds =  ('seedtest.superbtc.org')
    port = 18334