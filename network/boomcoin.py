from clove.network.bitcoin import Bitcoin


class Boomcoin(Bitcoin):
    """
    Class with all the necessary Boomcoin network information based on
    https://github.com/Boom-Coin/stealthboomcoin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'Boomcoin'
    symbols = ('BOOM', )
    seeds = ("107.170.88.155", "104.131.35.160")
    port = 28175

# Has no testnet
