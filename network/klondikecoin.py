from clove.network.bitcoin import Bitcoin


class KlondikeCoin(Bitcoin):
    """
    Class with all the necessary KlondikeCoin network information based on
    https://github.com/kittehcoin/kittehcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'klondikecoin'
    symbols = ('KDC', )
    seeds = ("dnsseed.klondikecoin.com",
             "dnsseed2.klondikecoin.com")
    port = 56680


class KlondikeCoinTestNet(KlondikeCoin):
    """
    Class with all the necessary KlondikeCoin testing network information based on
    https://github.com/kittehcoin/kittehcoin/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'test-klondikecoin'
    seeds = ("testnet-seed.klondikecointools.com",
             "testnet-seed.weminemnc.com")
    port = 19333
