from clove.network.bitcoin import Bitcoin


class MetalCoin(Bitcoin):
    """
    Class with all the necessary MetalCoin network information based on
    https://github.com/metalde/metalcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'metalcoin'
    symbols = ('METAL', )
    seeds = ('104.236.4.12')
    port = 22332


# Has no testnet