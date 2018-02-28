from clove.network.bitcoin import Bitcoin


class FirstCoin(Bitcoin):
    """
    Class with all the necessary FirstCoin network information based on
    https://github.com/firstcoinofficial/firstcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'firstcoin'
    symbols = ('FRST', )
    seeds = ("108.179.227.118")
    port = 10667


class FirstCoinTestNet(FirstCoin):
    """
    Class with all the necessary FirstCoin testing network information based on
    https://github.com/firstcoinofficial/firstcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'test-firstcoin'
    seeds = ("192.168.200.100")
    port = 10667
