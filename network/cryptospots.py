from clove.network.bitcoin import Bitcoin


class CryptoSpots(Bitcoin):
    """
    Class with all the necessary CryptoSpots network information based on
    https://github.com/xPooky/CryptoSpots/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'cryptospots'
    symbols = ('CS', )
    seeds = ("45.55.243.122",
             "104.236.84.239",
             "104.236.83.193")
    port = 17771

# Has no testnet
