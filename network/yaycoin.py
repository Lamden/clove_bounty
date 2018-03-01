from clove.network.bitcoin import Bitcoin


class YAYcoin(Bitcoin):
    """
    Class with all the necessary YAYcoin network information based on
    https://github.com/dkwzjw/yaycoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'yaycoin'
    symbols = ('YAY', )
    seeds = ("yaycoin.sun.ddns.vc",
             "yaycoin.luna.ddns.vc")
    port = 7785


class YAYcoinTestNet(YAYcoin):
    """
    Class with all the necessary YAYcoin testing network information based on
    https://github.com/dkwzjw/yaycoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-yaycoin'
    seeds = ("yaycoin.sun.ddns.vc",
             "yaycoin.luna.ddns.vc")
    port = 17785
