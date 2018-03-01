from clove.network.bitcoin import Bitcoin


class Peacecoin(Bitcoin):
    """
    Class with all the necessary Peacecoin network information based on
    https://github.com/peacedevelop/peacecoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'peacecoin'
    symbols = ('PEC', )
    seeds = ("coingen-seed-scrypt.bluematt.me")
    port = 1945


class PeacecoinTestNet(Bitcoin):
    """
    Class with all the necessary Peacecoin testing network information based on
    https://github.com/peacedevelop/peacecoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-peacecoin'
    seeds = ("testnet-seed.peacecoin.petertodd.org",
             "testnet-seed.bluematt.me")
    port = 11945
