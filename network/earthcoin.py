from clove.network.bitcoin import Bitcoin


class EarthCoin(Bitcoin):
    """
    Class with all the necessary EarthCoin network information based on
    https://github.com/earthcoinproject/earthcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'earthcoin'
    symbols = ('EAC', )
    seeds = ("dnsseed.earthcointools.org")
    port = 15677


class EarthCoinTestNet(EarthCoin):
    """
    Class with all the necessary EarthCoin testing network information based on
    https://github.com/earthcoinproject/earthcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-earthcoin'
    seeds = ("testnet-seed.earthcointools.org")
    port = 25677
