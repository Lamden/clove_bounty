from clove.network.bitcoin import Bitcoin


class Theresamaycoin(Bitcoin):
    """
    Class with all the necessary Theresa May Coin (MAY) network information based on
    https://github.com/zulufourm1ke/theresamaycoin-v1.0.1.0/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'theresamaycoin'
    symbols = ('MAY', )
    seeds = ('86.53.121.36')
    port = 35010


class TheresamaycoinTestNet(Theresamaycoin):
    """
    Class with all the necessary Theresa May Coin (MAY) testing network information based on
    https://github.com/zulufourm1ke/theresamaycoin-v1.0.1.0/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-theresamaycoin'
    seeds = ()
    port = 25714
