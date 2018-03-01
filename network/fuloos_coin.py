from clove.network.bitcoin import Bitcoin


class Fuloos_Coin(Bitcoin):
    """
    Class with all the necessary Fuloos Coin network information based on
    https://github.com/fuloos/Fuloos/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'fuloos_coin'
    symbols = ('FLS', )
    seeds = ("13.126.185.194",
             "13.127.56.191",
             "13.127.51.168",
             "138.68.236.172",
             "139.59.72.104",
             "35.154.71.99",
             "159.89.7.107",
             "159.89.7.115",
             "165.227.33.92",
             "165.227.33.93",
             "139.59.110.168",
             "139.59.110.185",
             "34.214.148.145",
             "52.62.108.155",
             "54.153.229.81")
    port = 11217
