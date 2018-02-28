from clove.network.bitcoin import Bitcoin


class Tychocoin(Bitcoin):
    """
    Class with all the necessary Tychocoin network information based on
    https://github.com/tychocoin2017/tychocoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'tychocoin'
    symbols = ('TYCHO', )
    seeds = ("50.63.164.183")
    port = 9333


class TychocoinTestNet(Tychocoin):
    """
    Class with all the necessary Tychocoin testing network information based on
    https://github.com/tychocoin2017/tychocoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-tychocoin'
    seeds = ("50.63.164.183")
    port = 19333
