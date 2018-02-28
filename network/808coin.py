from clove.network.bitcoin import Bitcoin


class Eight08Coin(Bitcoin):
    """
    Class with all the necessary  808Coin (808) network information based on
    https://github.com/maxxine/808/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = '808coin'
    symbols = ('808', )
    seeds = ('dns.808bass.space')
    port = 8087


class Eight08CoinTestNet(Eight08Coin):
    """
    Class with all the necessary  808Coin (808) network information based on
    https://github.com/maxxine/808/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-808coin'
    symbols = ('808', )
    seeds = ()
    port = 6903
