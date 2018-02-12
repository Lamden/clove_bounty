from clove.network.bitcoin import Bitcoin


class KushCoin(Bitcoin):
    """
    Class with all the necessary KushCoin network information based on
    https://github.com/kushcoin-project/kushcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'kushcoin'
    symbols = ('KUSH', )
    seeds = ("seed-a.kushcoin.co","seed-b.kushcoin.co")
    port = 31544


# Has no testnet