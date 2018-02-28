from clove.network.bitcoin import Bitcoin


class DarkGold(Bitcoin):
    """
    Class with all the necessary DarkGold network information based on
    https://github.com/darkgoldcoin/darkgoldcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'darkgold'
    symbols = ('DGD', )
    seeds = ("seed1.Darkgold.eu",
             "87.121.52.144",
             "88.213.221.50",
             "24.37.155.182",
             "176.58.99.41",
             "144.76.238.2",
             "37.59.24.15",
             "37.187.155.143",
             "104.236.43.108",
             "67.215.11.195",
             "192.95.29.153")
    port = 8855

# no testnet
