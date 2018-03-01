from clove.network.bitcoin import Bitcoin


class IslaCoin(Bitcoin):
    """
    Class with all the necessary IslaCoin network information based on
    https://github.com/islacoin/islacoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'islacoin'
    symbols = ('ISL', )
    seeds = ("seed1.islacoin.net", "seed2.islacoin.net", "seed3.islacoin.net")
    port = 9731


# Has no testnet
