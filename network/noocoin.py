from clove.network.bitcoin import Bitcoin


class NooCoin(Bitcoin):
    """
    Class with all the necessary NooCoin network information based on
    https://github.com/neureal/noocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'noocoin'
    symbols = ('NOO', )
    seeds = ("noocoin.iico.in",
             "home.bown.net",
             "j.iico.in")

    port = 41800


class NooCoinTestNet(NooCoin):
    """
    Class with all the necessary NooCoin testing network information based on
    https://github.com/neureal/noocoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-noocoin'
    seeds = ("noocoin.iico.in",
             "home.bown.net",
             "j.iico.in")
    port = 41810
