from clove.network.bitcoin import Bitcoin


class HiCoin(Bitcoin):
    """
    Class with all the necessary HiCoin network information based on
    https://github.com/hicoindev/hicoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'hicoin'
    symbols = ('XHI', )
    seeds = ('45.32.35.123')
    port = 35289


# Has no Testnet
