from clove.network.bitcoin import Bitcoin


class ApexCoin(Bitcoin):
    """
    Class with all the necessary ApexCoin network information based on
    https://github.com/apexdev/apexcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'ApexCoin'
    symbols = ('APEX', )
    seeds = ("62.116.254.204",
             "162.243.118.225",
             "5.9.23.116",
             "67.215.11.195")
    port = 19971

# Has no testnet
