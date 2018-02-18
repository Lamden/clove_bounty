from clove.network.bitcoin import Bitcoin


class DayTrader_Coin(Bitcoin):
    """
    Class with all the necessary DayTrader_Coin network information based on
    https://github.com/DayTraderCoin/DayTraderCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'daytrader_coin'
    symbols = ('DTC', )
    seeds = ("54.94.154.243",
             "54.207.102.95")
    port = 39110
	