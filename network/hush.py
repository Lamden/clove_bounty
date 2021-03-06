from clove.network.bitcoin import Bitcoin


class Hush(Bitcoin):
    """
    Class with all the necessary Hush network information based on
    https://github.com/MyHush/hush/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'hush'
    symbols = ('HUSH', )
    seeds = ("zdash.suprnova.cc", )
    port = 8888


class HushTestNet(Hush):
    """
    Class with all the necessary Hush testing network information based on
    https://github.com/MyHush/hush/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-hush'
    seeds = ("tush.cryptominingpools.org",
             "testnet.myhush.network",
             "testnet.madmining.club")
    port = 18888
