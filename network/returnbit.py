from clove.network.bitcoin import Bitcoin


class ReturnBit(Bitcoin):
    """
    Class with all the necessary ReturnBit network information based on
    https://github.com/Returnbit/Returnbit/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'returnbit'
    symbols = ('RBIT', )
    seeds = ("159.203.109.115",
             "45.55.167.126",
             "159.203.106.65")
    port = 9313


class ReturnBitTestNet(ReturnBit):
    """
    Class with all the necessary ReturnBit testing network information based on
    https://github.com/Returnbit/Returnbit/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-diamond'
    seeds = ("107.170.12.152",
             "159.203.109.115",
             "37.59.24.15",
             "216.106.225.215")
    port = 19113
