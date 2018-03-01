from clove.network.bitcoin import Bitcoin


class Lemanum(Bitcoin):
    """
    Class with all the necessary Lemanum network information based on
    https://github.com/lemanum/LMN/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'lemanum'
    symbols = ('LMN', )
    seeds = ("37.139.2.62",
             "107.185.68.254",
             "109.236.215.17",
             "116.91.31.66",
             "124.183.68.227",
             "130.255.12.106",
             "147.135.130.119",
             "153.213.96.231",
             "171.7.58.246",
             "46.4.88.116",
             "5.228.232.59",
             "95.78.98.68")
    port = 55993


class LemanumTestNet(Lemanum):
    """
    Class with all the necessary Lemanum testing network information based on
    https://github.com/lemanum/LMN/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'test-lemanum'
    seeds = ("107.22.138.243")
    port = 26178
