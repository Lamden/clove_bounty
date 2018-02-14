from clove.network.bitcoin import Bitcoin


class Chronos(Bitcoin):
    """
    Class with all the necessary Chronos network information based on
    https://github.com/chronoscoin/Chronoscoin/blob/Coin/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'chronos'
    symbols = ('CRX', )
    seeds = ("199.127.226.174",
             "89.207.129.108")
    port = 7633

# Has no testnet