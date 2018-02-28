from clove.network.bitcoin import Bitcoin


class Kittehcoin(Bitcoin):
    """
    Class with all the necessary Kittehcoin network information based on
    https://github.com/kittehcoin/kittehcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kittehcoin'
    symbols = ('MEOW', )
    seeds = ("dnsseed.kittehcoin.info",
             "dnsseed.kittehcoinwallet.com",
             "dnsseed.kittehcoinblockexplorer.com",
             "dnsseed.kittehcoinpool.com")
    port = 22566


class KittehcoinTestNet(Kittehcoin):
    """
    Class with all the necessary Kittehcoin testing network information based on
    https://github.com/kittehcoin/kittehcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-kittehcoin'
    seeds = ("dnsseed.kittehcoinblockexplorer.com")
    port = 44566
