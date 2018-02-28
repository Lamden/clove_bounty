from clove.network.bitcoin import Bitcoin


class mMXVI(Bitcoin):
    """
    Class with all the necessary MMXVI network information based on
    https://github.com/coin2016/mmxvi/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'MMXVI'
    symbols = ('MMXVI', )
    seeds = ("5.196.67.100")
    port = 6503


# Has no Testnet
