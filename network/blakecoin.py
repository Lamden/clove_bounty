from clove.network.bitcoin import Bitcoin


class Blakecoin(Bitcoin):
    """
    Class with all the necessary Blakecoin network information based on
    https://github.com/BlueDragon747/Blakecoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'blakecoin'
    symbols = ('BLC', )
    seeds = ("blakecoin.org",
             "blakecoin.com")
    port = 8773


class BlakecoinTestNet(Blakecoin):
    """
    Class with all the necessary Blakecoin testing network information based on
    https://github.com/BlueDragon747/Blakecoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-blakecoin'
    seeds = ("blakecoin.org",
             "blakecoin.com")
    port = 18773
