from clove.network.bitcoin import Bitcoin


class Slothcoin(Bitcoin):
    """
    Class with all the necessary Slothcoin (SLOTH) network information based on
    https://github.com/FibaX/Slothcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'slothcoin'
    symbols = ('SLOTH', )
    seeds = ('80.112.144.8', '82.139.127.205', '80.112.172.234', '173.209.34.107', '198.23.161.59')
    port = 5107


class SlothcoinTestNet(Slothcoin):
    """
    Class with all the necessary Slothcoin (SLOTH) testing network information based on
    https://github.com/FibaX/Slothcoin/blob/master/src/net.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-slothcoin'
    seeds = ('80.112.144.8', '82.139.127.205', '80.112.172.234', '173.209.34.107', '198.23.161.59')
    port = 15107
