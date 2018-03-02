from clove.network.bitcoin import Bitcoin


class DayTraderCoin(Bitcoin):
    """
    Class with all the necessary DayTrader_Coin network information based on
    https://github.com/DayTraderCoin/DayTraderCoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'daytrader_coin'
    symbols = ('DTC', )
    nodes = ("54.94.154.243",
             "54.207.102.95")
    port = 39110
    message_start = b'\x3e\x2f\xb4\xd5'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 218
    }
