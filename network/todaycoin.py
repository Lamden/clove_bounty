
from clove.network.bitcoin import Bitcoin


class TodayCoin(Bitcoin):
    """
    Class with all the necessary TODAY network information based on
    http://www.github.com/todayimage/todayimage-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'todaycoin'
    symbols = ('TODAY', )
    seeds = ('node.104.238.185.61',)
    port = 7869


class TodayCoinTestNet(TodayCoin):
    """
    Class with all the necessary TODAY testing network information based on
    http://www.github.com/todayimage/todayimage-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-todaycoin'
    seeds = ()
    port = 17869
