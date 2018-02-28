from clove.network.bitcoin import Bitcoin


class ATCCoin(Bitcoin):
    """
    Class with all the necessary ATC Coin network information based on
    https://github.com/atccoin2017/atccoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'atccoin'
    symbols = ('ATCC', )
    seeds = ("166.62.123.137")
    port = 9333


class ATCCoinTestNet(ATCCoin):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/atccoin2017/atccoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'test-atccoin'
    seeds = ("166.62.123.137")
    port = 19333
