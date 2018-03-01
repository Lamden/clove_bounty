from clove.network.bitcoin import Bitcoin


class GoldPressedLatinum(Bitcoin):
    """
    Class with all the necessary GoldPressedLatinum network information based on
    https://github.com/scificrypto/gold-pressed-latinum/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'goldpressedlatinum'
    symbols = ('GPL', )
    seeds = ("seed.goldpressedlatinum.su")
    port = 23635


# Has no testnet
