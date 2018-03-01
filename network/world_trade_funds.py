from clove.network.bitcoin import Bitcoin


class World_Trade_Funds(Bitcoin):
    """
    Class with all the necessary World Trade Funds network information based on
    https://github.com/wtfteam/wtfcoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'world_trade_funds'
    symbols = ('XWT', )
    seeds = ("107.170.189.185",
             "144.76.139.212")
    port = 42733
