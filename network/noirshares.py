from clove.network.bitcoin import Bitcoin


class NoirShares(Bitcoin):
    """
    Class with all the necessary NoirShares network information based on
    https://github.com/Nameshar/NoirShares/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'noirshares'
    symbols = ('NRS', )
    seeds = ("107.170.254.5",
             "192.241.213.244",
             "172.245.183.30",
             "162.243.131.88",
             "54.213.71.178",
             "192.241.213.224",
             "254.80.61.11",
             "198.199.96.129",
             "54.197.175.238",
             "54.244.236.250",
             "54.197.232.168")
    port = 8500
