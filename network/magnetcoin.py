from clove.network.bitcoin import Bitcoin


class Magnetcoin(Bitcoin):
    """
    Class with all the necessary Magnetcoin network information based on
    https://github.com/magnetcoindev/magnetcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'magnetcoin'
    symbols = ('MAGN', )
    seeds = ('96.44.173.109')
    port = 22458


# Has no testnet