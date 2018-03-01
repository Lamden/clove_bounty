from clove.network.bitcoin import Bitcoin


class HighVoltage(Bitcoin):
    """
    Class with all the necessary HighVoltage network information based on
    https://github.com/highvoltagecoin/highvoltagecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'highvoltage'
    symbols = ('HVCO', )
    seeds = ("seeder1.highvoltagecoin.tech", "seeder2.highvoltagecoin.tech")
    port = 47824


# has no testnet
