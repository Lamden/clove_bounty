from clove.network.bitcoin import Bitcoin


class BoxyCoin(Bitcoin):
    """
    Class with all the necessary BoxyCoin network information based on
    https://github.com/boxycoin/BoxyCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'boxycoin'
    symbols = ('BOXY', )
    seeds = ("boxy.online", "159.203.161.244",
             "pool.boxy.online", "198.199.124.131",
             "node.bubtails.com", "147.135.130.119",
             "boxycoin.ddns.net", "138.68.174.82",
             "electrum.boxy.online", "211.28.42.157")
    port = 21524


class BoxyCoinTestNet(BoxyCoin):
    """
    Class with all the necessary BoxyCoin testing network information based on
    https://github.com/boxycoin/BoxyCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-boxycoin'
    seeds = ("testnet-seed.boxy.online",
             "testnet-seed.boxycoin.org")
    port = 121524
