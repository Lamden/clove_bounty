from clove.network.bitcoin import Bitcoin


class BitLuckCoin(Bitcoin):
    """
    Class with all the necessary BitLuckCoin network information based on
    https://github.com/bitluckdev/bitluckcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitluckcoin'
    symbols = ('BTLC', )
    seeds = ("45.32.35.123", "45.76.96.149")
    port = 24289

# Has no testnet
