from clove.network.bitcoin import Bitcoin


class IOcoin(Bitcoin):
    """
    Class with all the necessary IOcoin network information based on
    https://github.com/IOCoin/iocoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'iocoin'
    symbols = ('IOC', )
    seeds = ("seed.iocoin.io",
             "seed1.iocoin.io",
             "seed2.iocoin.io")
    port = 33764

# no testnet
